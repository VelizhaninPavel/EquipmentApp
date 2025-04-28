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

// функция для отображения данных
function displayResults(data) {
    resultsDiv.innerHTML = ''; // очистка предыдущих результатов

    if (data.length === 0) {
        resultsDiv.innerHTML = 'Ничего не найдено.';
        return;
    }

    data.forEach(item => {
        const div = document.createElement('div');
        div.textContent = `Название: ${item.e_name} | Цех: ${item.l_id.l_shop} | Участок: ${item.l_id.l_area}`;
        resultsDiv.appendChild(div);
    });
}
