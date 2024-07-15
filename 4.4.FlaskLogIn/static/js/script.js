document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('table-select').addEventListener('change', function () {
        const tableName = this.value;
        if (tableName) {
            fetch('/get_table_data', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ table_name: tableName })
            })
            .then(response => response.json())
            .then(data => {
                renderTable(data.columns, data.rows);
            })
            .catch(error => {
                console.error('Error fetching table data:', error);
            });
        }
    });

    function renderTable(columns, rows) {
        const headers = document.getElementById('table-headers');
        const body = document.getElementById('table-body');
    
        headers.innerHTML = '';
        body.innerHTML = '';
    
        // Create table headers including the new button column
        columns.forEach((col, index) => {
            const th = document.createElement('th');
            th.textContent = col;
            th.dataset.index = index;
            th.addEventListener('click', () => sortTable(index));
            headers.appendChild(th);
        });
    
        // Add header for the new button column
        const th = document.createElement('th');
        th.textContent = 'Actions'; // Customize as needed
        headers.appendChild(th);
    
        // Create table rows
        rows.forEach(rowData => {
            const tr = document.createElement('tr');
    
            // Create cells for existing columns
            rowData.forEach(cellData => {
                const td = document.createElement('td');
                td.textContent = cellData;
                tr.appendChild(td);
            });
    
            // Create cell for the new button column
            const td = document.createElement('td');
            const editBtn = document.createElement('button');
            editBtn.textContent = 'Edit'; // Button text, customize as needed
            editBtn.classList.add('edit-btn'); // Add class for styling and event handling
            editBtn.addEventListener('click', () => handleEdit(tr)); // Add event listener for edit functionality
            td.appendChild(editBtn);
            tr.appendChild(td);
    
            // Append row to table body
            body.appendChild(tr);
        });
    }
    
    function sortTable(index) {
        const table = document.getElementById('data-table');
        const rows = Array.from(table.rows).slice(1); // Exclude header row
        const header = table.rows[0].cells[index];
        const isAscending = header.classList.contains('sorted-asc');

        // Remove sorting indicators from all headers
        const allHeaders = table.querySelectorAll('th');
        allHeaders.forEach(th => {
            th.classList.remove('sorted-asc', 'sorted-desc');
        });

        // Toggle sorted class for the clicked header
        header.classList.toggle('sorted-asc', !isAscending);
        header.classList.toggle('sorted-desc', isAscending);

        rows.sort((rowA, rowB) => {
            const cellA = rowA.cells[index].textContent.trim();
            const cellB = rowB.cells[index].textContent.trim();
            
            if (isAscending) {
                return cellA.localeCompare(cellB, undefined, { numeric: true });
            } else {
                return cellB.localeCompare(cellA, undefined, { numeric: true });
            }
        });

        // Append sorted rows back to table body
        rows.forEach(row => table.appendChild(row));
    }
});
