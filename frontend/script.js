/* Список всего оборудования (модальное окно) */

const fullListLink = document.getElementById('fullListLink');
const fullListModal = document.getElementById('fullListModal');
const fullListModalClose = document.getElementById('fullListModalClose');
const fullListResults = document.getElementById('fullListResults');

// Открыть модалку полного списка
fullListLink.addEventListener('click', (event) => {
    event.preventDefault();
    fetchAllEquipment();
});

// Закрыть модалку
fullListModalClose.addEventListener('click', () => {
    fullListModal.style.display = 'none';
});

// Закрыть модалку по клику вне области
window.addEventListener('click', (event) => {
    if (event.target === fullListModal) {
        fullListModal.style.display = 'none';
    }
});

// Получение всех данных оборудования
function fetchAllEquipment() {
    fetch('http://127.0.0.1:8000/api/v1/equipment/')
        .then(response => response.json())
        .then(data => {
            showFullList(data);
            fullListModal.style.display = 'block';
        })
        .catch(error => {
            console.error('Ошибка при загрузке полного списка:', error);
        });
}

// Показать компактные карточки
function showFullList(data) {
    fullListResults.innerHTML = '';

    data.forEach(item => {
        const card = document.createElement('div');
        card.classList.add('compact-card');

        card.innerHTML = `
            <p><strong>${item.e_name}</strong></p>
            <p>Местоположение: ${item.l_id.l_shop} - ${item.l_id.l_area}</p>
            <p>Тип оборудования: ${item.t_type.t_type}</p>
        `;

        fullListResults.appendChild(card);
    });
}
