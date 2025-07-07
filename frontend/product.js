const api = "http://127.0.0.1:8000/products";

function switchMode() {
  document.querySelectorAll(".crud-box").forEach(box => box.style.display = "none");
  const mode = document.getElementById("crudSelect").value;
  if (mode) document.getElementById(mode + "Box").style.display = "block";
}

async function createProduct_line() {
  const product_line = {
    name: document.getElementById("c_name").value,
    factory: document.getElementById("c_catagory").value,
    status: document.getElementById("c_price").value,
    capacity_per_day: parseInt(document.getElementById("c_capacity_per_day").value) || 0,
  };
  try {
    await axios.post(api, product_line);
    alert("✅ 新增成功");
  } catch (err) {
    alert("❌ 錯誤：" + (err.response?.data?.detail || err.message));
  }
}

async function readProduct_line() {
  const keyword = document.getElementById("r_keyword").value.toLowerCase();
  const res = await axios.get(api);
  const table = document.getElementById("readTable");
  table.innerHTML = "";
  res.data.forEach(f => {
  if (f.name.toLowerCase().includes(keyword)) {
    table.innerHTML += `<tr>
      <td>${f.line_id}</td><td>${f.name}</td>
      <td>${f.factory_id}</td><td>${f.status}</td>
      <td>${f.ecapacity_per_day || ""}</td>
    </tr>`;
    }
  });
}

async function loadUpdateProduct_line() {
  const id = document.getElementById("u_id").value;
  try {
    const res = await axios.get(`${api}/${id}`);
    const f = res.data;
    document.getElementById("u_name").value = f.name;
    document.getElementById("u_factory").value = f.factory_id;
    document.getElementById("u_status").value = f.status;
    document.getElementById("u_capacity_per_day").value = f.capacity_per_day || "";
    document.getElementById("updateForm").style.display = "block";
  } catch (err) {
    alert("❌ 找不到工廠");
    document.getElementById("updateForm").style.display = "none";
  }
}

async function updateProduct_line() {
  const id = document.getElementById("u_id").value;
  const product_line = {
    name: document.getElementById("u_name").value,
    factory_id: document.getElementById("u_factory").value,
    status: document.getElementById("u_status").value,
    capacity_per_day: parseInt(document.getElementById("u_capacity_per_day").value) || 0,
  };
  try {
    await axios.put(`${api}/${id}`, product_line);
    alert("✅ 修改成功");
  } catch (err) {
    alert("❌ 修改失敗：" + err.message);
  }
}

async function deleteProduct_line() {
  const id = document.getElementById("d_id").value;
  if (!confirm(`確定要刪除工廠 ID ${id} 嗎？`)) return;
    try {
      await axios.delete(`${api}/${id}`);
      alert("✅ 刪除成功");
    } catch (err) {
      alert("❌ 刪除失敗：" + err.message);
  }
}