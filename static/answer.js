document.addEventListener('DOMContentLoaded', function () {
    // Create the notification
    const notification = document.createElement('div');
    notification.className = 'notification show';
    notification.textContent = 'Welcome to UHelper! Enjoy your visit.';

    // Append the notification to the body
    document.body.appendChild(notification);

    // Automatically remove the notification after 5 seconds
    setTimeout(() => {
        notification.classList.remove('show'); // Start fade-out effect
        setTimeout(() => document.body.removeChild(notification), 500); // Remove after fade-out
    }, 5000);
});
