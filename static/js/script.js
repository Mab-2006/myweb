function sendMessage() {
    let userName = document.getElementById('userName').value;
    let userEmail = document.getElementById('userEmail').value;

    if (!userName || !userEmail) return;

    // نمایش پیام کاربر در چت
    let chatBox = document.getElementById('chatBox');
    chatBox.innerHTML += `<div class="message user-message">${userName} - ${userEmail}</div>`;

    // ارسال داده به سرور (Flask)
    fetch('/send', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name: userName, email: userEmail })
    })
    .then(response => response.json())
    .then(data => {
        chatBox.innerHTML += `<div class="message bot-message">${data.message}</div>`;
    });

    // پاک کردن فیلد ورودی
    document.getElementById('userName').value = '';
    document.getElementById('userEmail').value = '';
}
