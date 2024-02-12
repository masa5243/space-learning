console.log("disofduo")
// 入力と学習のページ切り替え------------
document.addEventListener('DOMContentLoaded', () => {
  const toggleSwitch = document.querySelector('#toggle-switch');
  const mainContainer = document.querySelector('.input-page');
  const sectionContainer = document.querySelector('.learning-page');

  toggleSwitch.addEventListener('change', () => {
      if (toggleSwitch.checked) {
          mainContainer.style.display = 'none'; // mainを表示
          sectionContainer.style.display = 'block'; // sectionを非表示
      } else {
          mainContainer.style.display = 'block'; // mainを非表示
          sectionContainer.style.display = 'none'; // sectionを表示
      }
  });
});
// ここまでが切り替え-------------------

// // // フォームの転送処理--------------------
// // フォームのsubmitイベントをキャンセル
document.getElementById('control-button').addEventListener('click', function(event) {
  event.preventDefault(); // デフォルトの送信動作を停止

  // FormDataオブジェクトを作成し、フォームデータを収集
  const formData = new FormData(document.querySelector('form')); // form要素を直接指定

  // クイズと答えの入力フィールドを取得し、FormDataに追加
  const quizzes = document.querySelectorAll('[name="quiz[]"]');
  const answers = document.querySelectorAll('[name="answer[]"]');

  quizzes.forEach((quizInput, index) => {
    const answerInput = answers[index]; // 対応するanswerInputを取得
    if (quizInput.value && answerInput.value) {
      formData.append('quiz[]', quizInput.value);
      formData.append('answer[]', answerInput.value);
    }
  });

  // リクエストを送信
  fetch('/submit_data', {
    method: 'POST',
    body: formData
  })
  .then(response => response.text())
  .then(data => console.log(data))
  .catch(error => console.log("ng", error));
});



function addRow() {
  const quizForm = document.getElementById("quizForm");
  const newQuizEntry = quizForm.getElementsByClassName("quiz-entry")[0].cloneNode(true);
  newQuizEntry.getElementsByTagName("input")[0].value = "";
  newQuizEntry.getElementsByTagName("input")[1].value = "";
  // 作成ボタンの直前に新しいエントリを挿入
  const createButton = document.querySelector(".quiz-create");
  quizForm.insertBefore(newQuizEntry, createButton);
}


function deleteRow(button) {
  button.parentNode.parentNode.remove();
}



// document.addEventListener('DOMContentLoaded', function() {
//   const dateInput = document.getElementById('date');
//   const today = new Date().toISOString().substring(0, 10);
//   dateInput.value = today;
//   const form = document.querySelector('form');
//   form.onsubmit = function(event) {
//     event.preventDefault(); // ページのリロードを防ぐ

//     // FormDataオブジェクトを作成
//     const formData = new FormData(form);
    
//     // fetchを使って非同期リクエストを送信
//     fetch('http://127.0.0.1:5000/submit_data', {
//       method: 'POST',
//       body: formData
//     })
//     .then(response => {
//       if (!response.ok) {
//         throw new Error('Network response was not ok');
//       }
//       return response.text();
//     })
//     .then(data => console.log(data))
//     .catch(error => console.error('Error:', error));
//   };
// });
// // ここまでがフォーム転送-------------




