const api = "http://localhost:8000/employees";

    function switchMode() {
      document.querySelectorAll(".crud-box").forEach(box => box.style.display = "none");
      const mode = document.getElementById("crudSelect").value;
      if (mode) document.getElementById(mode + "Box").style.display = "block";
    }

    async function createEmployee() {
      const employee = {
        factory_id: parseInt(document.getElementById("c_factory_id").value),
        name: document.getElementById("c_name").value,
        position: document.getElementById("c_position").value,
        phone: document.getElementById("c_phone").value,
        hire_date: document.getElementById("c_hire_date").value
      };
      try {
        await axios.post(api, employee);
        alert("✅ 新增成功");
      } catch (err) {
        alert("❌ 錯誤：" + (err.response?.data?.detail || err.message));
      }
    }

    async function readEmployees() {
      const keyword = document.getElementById("r_keyword").value.toLowerCase();
      const res = await axios.get(api);
      const table = document.getElementById("readTable");
      table.innerHTML = "";
      res.data.forEach(e => {
        if (e.name.toLowerCase().includes(keyword)) {
          table.innerHTML += `<tr>
            <td>${e.employee_id}</td><td>${e.name}</td>
            <td>${e.factory_id}</td><td>${e.position || ""}</td>
            <td>${e.phone || ""}</td><td>${e.hire_date || ""}</td>
          </tr>`;
        }
      });
    }

    async function loadUpdateEmployee() {
      const id = document.getElementById("u_id").value;
      try {
        const res = await axios.get(`${api}/${id}`);
        const e = res.data;
        document.getElementById("u_factory_id").value = e.factory_id;
        document.getElementById("u_name").value = e.name;
        document.getElementById("u_position").value = e.position;
        document.getElementById("u_phone").value = e.phone;
        document.getElementById("u_hire_date").value = e.hire_date || "";
        document.getElementById("updateForm").style.display = "block";
      } catch (err) {
        alert("❌ 找不到員工");
        document.getElementById("updateForm").style.display = "none";
      }
    }

    async function updateEmployee() {
      const id = document.getElementById("u_id").value;
      const employee = {
        factory_id: parseInt(document.getElementById("u_factory_id").value),
        name: document.getElementById("u_name").value,
        position: document.getElementById("u_position").value,
        phone: document.getElementById("u_phone").value,
        hire_date: document.getElementById("u_hire_date").value
      };
      try {
        await axios.put(`${api}/${id}`, employee);
        alert("✅ 修改成功");
      } catch (err) {
        alert("❌ 修改失敗：" + err.message);
      }
    }

    async function deleteEmployee() {
      const id = document.getElementById("d_id").value;
      if (!confirm(`確定要刪除員工 ID ${id} 嗎？`)) return;
      try {
        await axios.delete(`${api}/${id}`);
        alert("✅ 刪除成功");
      } catch (err) {
        alert("❌ 刪除失敗：" + err.message);
      }
    }