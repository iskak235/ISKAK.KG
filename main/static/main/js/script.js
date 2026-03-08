// script.js
document.addEventListener('DOMContentLoaded', function() {
    console.log("Сайт ийгиликтүү иштеп жатат!");

    // Карталарды басканда жумшак эффект берүү
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.cursor = 'pointer';
        });
    });
});