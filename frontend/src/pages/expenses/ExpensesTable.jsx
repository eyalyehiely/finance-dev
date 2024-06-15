import React, { useState, useEffect } from 'react';
import axios from 'axios';
import swal from 'sweetalert';
import AddCommaToNumber from '../../components/AddComma';

function ExpensesTable() {
  const [expenses, setExpenses] = useState([]);
  const [editingExpenseId, setEditingExpenseId] = useState(null);
  const [editedExpense, setEditedExpense] = useState({});
  const [status, setStatus] = useState({});

  const token = localStorage.getItem('authTokens') ? JSON.parse(localStorage.getItem('authTokens')).access : null;

  function fetchData() {
    axios.post('http://localhost:8000/api/get_all_expenses/', {}, {
      headers: {
        'content-type': 'application/json',
        Authorization: `Bearer ${token}`,
      }
    })
      .then(response => {
        if (response.data.status === 200) {
          setExpenses(response.data.all_expenses);
        } else {
          console.log('Error:', response.data.message);
          swal({
            title: "Error!",
            text: `Frontend Error: ${response.data.message}`,
            icon: "warning",
            button: "OK",
          });
        }
      })
      .catch(error => {
        console.error('There was an error!', error);
        swal({
          title: "Error!",
          text: `Backend Error: ${error.message}`,
          icon: "error",
          button: "OK",
        });
      });
  }

  function deleteExpense(id) {
    swal({
      title: "האם אתה בטוח?",
      text: "ברגע שתלחץ על אישור לא יהיה ניתן לשחזר את המידע",
      icon: "warning",
      buttons: true,
      dangerMode: true,
    }).then((willDelete) => {
      if (willDelete) {
        axios.delete(`http://localhost:8000/api/delete_expense/${id}/`, {
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${token}`,
          }
        }).then((response) => {
          swal({
            title: "🗑️!עבודה טובה",
            text: " !ההוצאה נמחק בהצלחה",
            icon: "success",
            button: "אישור",
          }).then(() => {
            fetchData(); // Refresh the data after deletion
            window.location.reload()
          });
        }).catch((error) => {
          console.error("Error deleting expense:", error);
          swal({
            title: "Ⅹ!שגיאה ",
            text: "שגיאת שרת!",
            icon: "warning",
            button: "אישור",
          });
        });
      } else {
        swal("הנתונים שלך בטוחים");
      }
    });
  }
  

  function handleEditChange(event, field) {
    setEditedExpense({
      ...editedExpense,
      [field]: event.target.value
    });
  }

  function startEdit(expense) {
    setEditingExpenseId(expense.id);
    setEditedExpense(expense);
  }

  function saveEdit() {
    const editedData = {
      payment_method: editedExpense.payment_method,
      date_and_time: editedExpense.date_and_time,
      name: editedExpense.name,
      price: editedExpense.price.replace(/,/g, ''), // Remove commas before saving
      credit_card: editedExpense.credit_card || '',
    };

    axios.put(`http://localhost:8000/api/edit_expense/${editingExpenseId}/`, editedData, {
      headers: {
        'content-type': 'application/json',
        Authorization: `Bearer ${token}`,
      }
    })
      .then(response => {
        if (response.data.status === 200) {
          swal({
            title: "Success!",
            text: "Expense updated successfully!",
            icon: "success",
            button: "OK",
          });
          setExpenses(expenses.map(expense => expense.id === editingExpenseId ? response.data.expense : expense));
          setEditingExpenseId(null);
          fetchData();
        } else {
          console.log('Error:', response.data.message);
          alert(response.data.message); // Adjust error handling as needed
        }
      })
      .catch(error => {
        console.error('There was an error!', error);
        alert('An error occurred while updating the expense.'); // Adjust error handling as needed
      });
  }

  function getCreditData() {
    axios.post('http://localhost:8000/api/get_credit_card/', {},{
      headers: {
        'content-type': 'application/json',
        Authorization: `Bearer ${token}`,
      }
    })
      .then(response => {
        if (response.data.status === 200) {
          const cards = response.data.credit_cards ;
        } else {
          console.log('Error:', response.data.message);
          swal({
            title: "Ⅹ!שגיאה ",
            text: {"!שגיאת מערכת":response.data.message},
            icon: "warning",
            button: "אישור",
          })
        }
      })

      .catch(error => {
        console.error('There was an error!', error);
        swal({
          title: "Ⅹ!שגיאה ",
          text: {"!שגיאת backend":response.data.message},
          icon: "warning",
          button: "אישור",
        })
      });
  }









  function isCreditCard() {
    if (status === 'creditcard') {
      return (
          <div>
            {/* cards */}
            {/* <label className="block text-sm font-medium mb-1" htmlFor="life_status">
              משפחה <span className="text-rose-500">*</span>
            </label> */}
            <td className="p-2">
            cards.map()
              <select type="text" id="name" className="text-right" value={editedExpense.name} >

              </select>
            </td>
          </div>
      );
    }
  }









  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div className="bg-white dark:bg-slate-800 shadow-lg rounded-sm border border-slate-200 dark:border-slate-700 relative" dir="rtl">
      <header className="px-5 py-4">
        <h2 className="font-semibold text-slate-800 dark:text-slate-100">הוצאות <span className="text-slate-400 dark:text-slate-500 font-medium">{expenses.length}</span></h2>
      </header>
      <div className="overflow-x-auto" dir="rtl">
        <table className="table-auto w-full dark:text-slate-300">
          <thead className="text-xs uppercase text-slate-400 dark:text-slate-500 bg-slate-50 dark:bg-slate-700 dark:bg-opacity-50 rounded-sm">
            <tr>
              <th className="p-2">
                <div className="font-semibold text-right">מס״ד</div>
              </th>
              <th className="p-2">
                <div className="font-semibold text-right">שם ההוצאה</div>
              </th>
              <th className="p-2">
                <div className="font-semibold text-right">דרך תשלום</div>
              </th>
              <th className="p-2">
                <div className="font-semibold text-right">סכום</div>
              </th>
              <th className="p-2">
                <div className="font-semibold text-right">תאריך ההוצאה</div>
              </th>
              <th className="p-2">
                <div className="font-semibold text-right">פעולות</div>
              </th>
            </tr>
          </thead>
          <tbody className="text-sm font-medium divide-y divide-slate-100 dark:divide-slate-700">
            {expenses.length > 0 ? (
              expenses.map((expense, index) => (
                <tr key={expense.id}>
                  <td className="p-2">
                    <div className="text-right">{index + 1}</div>
                  </td>
                  {editingExpenseId === expense.id ? (
                    <>
                      <td className="p-2">
                        <input type="text" id="name" className="text-right" value={editedExpense.name} onChange={(e) => handleEditChange(e, 'name')} />
                      </td>
                      <td className="p-2">
                        <select id="payment_method" className="text-right" value={editedExpense.payment_method} onChange={(e) => handleEditChange(e, 'payment_method'), setStatus(e.target.value)}>
                          <option value=""></option>
                          <option value="credit_card">כרטיס אשראי</option>
                          <option value="direct_debit">הוראת קבע</option>
                          <option value="transaction">העברה בנקאית</option>
                          <option value="cash">מזומן</option>
                          <option value="check">צ׳ק</option>
                        </select>
                      </td>

                      {isCreditCard()}

                      <td className="p-2">
                        <input type="text" id="price" className="text-right" value={AddCommaToNumber(editedExpense.price)} onChange={(e) => handleEditChange(e, 'price')} />
                      </td>
                      <td className="p-2">
                        <input type="text" id="date_and_time" className="text-right" value={new Date(editedExpense.date_and_time).toLocaleString()} onChange={(e) => handleEditChange(e, 'date_and_time')} />
                      </td>
                      <td className="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap w-px">
                        <div className="space-x-1">
                          <button
                            className="text-slate-400 hover:text-slate-500 dark:text-slate-500 dark:hover:text-slate-400 rounded-full"
                            onClick={saveEdit}
                          >
                            <span className="sr-only">Save</span>
                            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="green" className="bi bi-check2-circle" viewBox="0 0 16 16">
                              <path d="M2.5 8a5.5 5.5 0 0 1 8.25-4.764.5.5 0 0 0 .5-.866A6.5 6.5 0 1 0 14.5 8a.5.5 0 0 0-1 0 5.5 5.5 0 1 1-11 0" />
                              <path d="M15.354 3.354a.5.5 0 0 0-.708-.708L8 9.293 5.354 6.646a.5.5 0 1 0-.708.708l3 3a.5.5 0 0 0 .708 0z" />
                            </svg>
                          </button>
                          <button
                            className="text-rose-500 hover:text-rose-600 squre-full"
                            onClick={() => setEditingExpenseId(null)}
                          >
                            <span className="sr-only">Cancel</span>
                            <svg className="w-10 h-6 fill-current" viewBox="0 0 32 32">
                              <path d="M16 2a14 14 0 1 0 14 14A14 14 0 0 0 16 2Zm7 19a1 1 0 0 1-1.414 1.414L16 17.414l-5.586 5.586A1 1 0 0 1 9 21.586l5.586-5.586L9 10.414A1 1 0 0 1 10.414 9l5.586 5.586 5.586-5.586A1 1 0 0 1 23 10.414l-5.586 5.586Z" />
                            </svg>
                          </button>
                        </div>
                      </td>
                    </>
                  ) : (
                    <>
                      <td className="p-2">
                        <div className="text-right">{expense.name}</div>
                      </td>
                      <td className="p-2">
                        <div className="text-right">{expense.payment_method}</div>
                      </td>
                      <td className="p-2">
                        <div className="text-right">{AddCommaToNumber(expense.price)}</div>
                      </td>
                      <td className="p-2">
                        <div className="text-right">{new Date(expense.date_and_time).toLocaleString()}</div>
                      </td>
                      <td className="px-2 first:pl-5 last:pr-5 py-3 whitespace-nowrap w-px">
                        <div className="space-x-1">
                          <button
                            className="text-slate-400 hover:text-slate-500 dark:text-slate-500 dark:hover:text-slate-400 rounded-full"
                            onClick={() => {
                              startEdit(expense);
                            }}
                          >
                            <span className="sr-only">Edit</span>
                            <svg className="w-8 h-8 fill-current" viewBox="0 0 32 32">
                              <path d="M19.7 8.3c-.4-.4-1-.4-1.4 0l-10 10c-.2.2-.3.4-.3.7v4c0 .6.4 1 1 1h4c.3 0 .5-.1.7-.3l10-10c.4-.4.4-1 0-1.4l-4-4zM12.6 22H10v-2.6l6-6 2.6 2.6-6 6zm7.4-7.4L17.4 12l1.6-1.6 2.6 2.6-1.6 1.6z" />
                            </svg>
                          </button>

                          <button
                            className="text-rose-500 hover:text-rose-600 rounded-full"
                            onClick={() => deleteExpense(expense.id)}
                          >
                            <span className="sr-only">Delete</span>
                            <svg className="w-8 h-8 fill-current" viewBox="0 0 32 32">
                              <path d="M13 15h2v6h-2zM17 15h2v6h-2z" />
                              <path d="M20 9c0-.6-.4-1-1-1h-6c-.6 0-1 .4-1 1v2H8v2h1v10c0 .6.4 1 1 1h12c.6 0 1-.4 1-1V13h1v-2h-4V9zm-6 1h4v1h-4v-1zm7 3v9H11v-9h10z" />
                            </svg>
                          </button>
                        </div>
                      </td>
                    </>
                  )}
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="6" className="p-2 text-center">
                  אין הוצאות להצגה
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>

    </div>
  );
}

export default ExpensesTable;
