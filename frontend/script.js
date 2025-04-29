// найти элементы
const searchInput = document.getElementById('equipment-search-input');
const searchButton = document.getElementById('equipment-search-button');
const resultsDiv = document.getElementById('equipment-results-container');


// обработчик клика на кнопку
searchButton.addEventListener('click', function() {
    const query = searchInput.value; // получаем текст из поиска

    // url запроса
    const apiUrl = `http://127.0.0.1:8000/api/v1/equipment/?search=${encodeURIComponent(query)}`;

    // get-запрос
    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('Ошибка запроса');
            }
            return response.json();
        })
        .then(data => {
            console.log(data); // посмотреть данные в консоли
            displayResults(data); // показать на странице
        })
        .catch(error => {
            console.error('Ошибка:', error);
            resultsDiv.innerHTML = 'Ошибка загрузки данных.';
        });
});


// функция для отображения данных в виде карточки

function displayResults(data) {
    data.forEach(item => {
        const card = document.createElement('div');
        card.classList.add('equipment-card');
        card.innerHTML = `
            <h3>${item.e_name}</h3>
            <p><strong>Местоположение:</strong> ${item.l_id.l_shop} - ${item.l_id.l_area}</p>
            <p><strong>Тип оборудования:</strong> ${item.t_type.t_type}</p>
        `;

        // вставляем новую карточку в самое начало
        resultsDiv.prepend(card);

        // eсли карточек стало больше 5 — удаляем последнюю
        const allCards = resultsDiv.querySelectorAll('.equipment-card');
        if (allCards.length > 5) {
            allCards[allCards.length - 1].remove();
        }
    });
}

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
