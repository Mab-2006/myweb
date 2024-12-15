function sendMessage() {
    let userName = document.getElementById('userName').value;
    let userEmail = document.getElementById('userEmail').value;

    if (!userName || !userEmail) return;

    let chatBox = document.getElementById('chatBox');
    chatBox.innerHTML += `<div class="message user-message">${userName} - ${userEmail}</div>`;

    fetch('/send', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: userName, email: userEmail })
    })
    .then(response => response.json())
    .then(data => {
        chatBox.innerHTML += `<div class="message bot-message">${data.message}</div>`;
    })
    .catch(error => {
        console.error('Error:', error);
        chatBox.innerHTML += `<div class="message bot-message">Error sending message, please try again.</div>`;
    });

    document.getElementById('userName').value = '';
    document.getElementById('userEmail').value = '';
}

window.addEventListener('load', () => {
    const preloader = document.getElementById('preloader');
    
    preloader.style.opacity = '0';
    
    setTimeout(() => {
        preloader.style.display = 'none';
        document.body.classList.add('loaded');
    }, 1000); 
});

window.addEventListener('scroll', () => {
    const elements = document.querySelectorAll('.scroll-animation');
    elements.forEach((element) => {
        const elementPosition = element.getBoundingClientRect().top;
        const screenPosition = window.innerHeight;

        if (elementPosition < screenPosition) {
            element.classList.add('visible');
        }
    });
});
