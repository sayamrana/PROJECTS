document.addEventListener('DOMContentLoaded', function () {
    const faqs = document.querySelectorAll('.faq');

    faqs.forEach(faq => {
        faq.querySelector('.ques').addEventListener('click', () => {
           
            faq.classList.toggle('active');
        });
    });
});