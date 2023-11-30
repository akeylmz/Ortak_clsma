src="https://code.jquery.com/jquery-3.6.0.min.js"
       
       
    icon = document.querySelector('.icon');
    search = document.querySelector('.search');
    icon.onclick = function(){
          search.classList.toggle('active')
      }
function clearSearch() {
    const input = document.getElementById('mysearch');
    input.value = '';
    searchTable(); // Temizle dÃ¼ÄŸmesine basÄ±ldÄ±ÄŸÄ±nda tabloyu sÄ±fÄ±rla
}
function searchTable() {
    const input = document.getElementById('mysearch');
    const filter = input.value.toUpperCase();
    const table = document.getElementById('table');
    const rows = table.getElementsByTagName('tr');

    for (let i = 1; i < rows.length; i++) {
        const cells = rows[i].getElementsByTagName('td');
        let found = false;

        for (let j = 0; j < cells.length; j++) {
            const cell = cells[j];

            if (cell) {
                const textValue = cell.textContent || cell.innerText;

                if (textValue.toUpperCase().indexOf(filter) > -1) {
                    found = true;
                    break; // Tek bir eÅŸleÅŸme yeterli
                }
            }
        }

        if (found) {
            rows[i].style.display = '';
        } else {
            rows[i].style.display = 'none';
        }
    }
}

function modalAc(){

}

//--------------------------------------------//


// Tablo scroll bar
const table = document.getElementById("table");

function checkTableHeight() {
  const tableContainer = document.querySelector(".lists");

  if (tableContainer.scrollHeight > tableContainer.clientHeight) {
    tableContainer.style.overflowY = "scroll";
  } else {
    tableContainer.style.overflowY = "hidden";
  }
}
window.addEventListener("load", checkTableHeight);
table.addEventListener("input", checkTableHeight);


function addUnit(inputId) {
    var inputElement = document.getElementById(inputId);
    var inputValue = inputElement.value;

    // Eğer değer boş değilse ve "kW" içermiyorsa, "kW" ekleyin
    if (inputValue !== "" && !inputValue.includes("kW")) {
        inputElement.value = inputValue + " kW";
    }
}



/* Dolar Kuru Çekme */

  
  
 