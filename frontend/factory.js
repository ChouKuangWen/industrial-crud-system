const api = "http://localhost:8000/factories";

function switchMode() {
  document.querySelectorAll(".crud-box").forEach(box => box.style.display = "none");
  const mode = document.getElementById("crudSelect").value;
  if (mode) document.getElementById(mode + "Box").style.display = "block";
}

async function createFactory() {
  const factory = {
    name: document.getElementById("c_name").value,
    location: document.getElementById("c_location").value,
    phone: document.getElementById("c_phone").value,
    employee_count: parseInt(document.getElementById("c_employee_count").value) || 0,
    established_date: document.getElementById("c_established_date").value
  };
  try {
    await axios.post(api, factory);
    alert("✅ 新增成功");
  } catch (err) {
    alert("❌ 錯誤：" + (err.response?.data?.detail || err.message));
  }
}

async function readFactories() {
  const keyword = document.getElementById("r_keyword").value.toLowerCase();
  const res = await axios.get(api);
  const table = document.getElementById("readTable");
  table.innerHTML = "";
  res.data.forEach(f => {
    if (f.name.toLowerCase().includes(keyword)) {
      table.innerHTML += `<tr>
        <td>${f.factory_id}</td><td>${f.name}</td>
        <td>${f.location || ""}</td><td>${f.phone || ""}</td>
        <td>${f.employee_count}</td><td>${f.established_date || ""}</td>
      </tr>`;
    }
  });
}

async function loadUpdateFactory() {
  const id = document.getElementById("u_id").value;
  try {
    const res = await axios.get(`${api}/${id}`);
    const f = res.data;
    document.getElementById("u_name").value = f.name;
    document.getElementById("u_location").value = f.location;
    document.getElementById("u_phone").value = f.phone;
    document.getElementById("u_employee_count").value = f.employee_count;
    document.getElementById("u_established_date").value = f.established_date || "";
    document.getElementById("updateForm").style.display = "block";
  } catch (err) {
    alert("❌ 找不到工廠");
    document.getElementById("updateForm").style.display = "none";
  }
}

async function updateFactory() {
  const id = document.getElementById("u_id").value;
  const factory = {
    name: document.getElementById("u_name").value,
    location: document.getElementById("u_location").value,
    phone: document.getElementById("u_phone").value,
    employee_count: parseInt(document.getElementById("u_employee_count").value) || 0,
    established_date: document.getElementById("u_established_date").value
  };
  try {
    await axios.put(`${api}/${id}`, factory);
    alert("✅ 修改成功");
  } catch (err) {
    alert("❌ 修改失敗：" + err.message);
  }
}

async function deleteFactory() {
  const id = document.getElementById("d_id").value;
  if (!confirm(`確定要刪除工廠 ID ${id} 嗎？`)) return;
  try {
    await axios.delete(`${api}/${id}`);
    alert("✅ 刪除成功");
  } catch (err) {
    alert("❌ 刪除失敗：" + err.message);
  }
}