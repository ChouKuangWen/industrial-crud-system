const api = "http://localhost:8000/records";
function switchMode() {
  document.querySelectorAll(".crud-box").forEach(box => box.style.display = "none");
  const mode = document.getElementById("crudSelect").value;
  if (mode) document.getElementById(mode + "Box").style.display = "block";
}

async function createProduct_record() {
  const product_record = {
  line_id: document.getElementById("c_line_id").value,
  product_id: document.getElementById("c_product_id").value,
  produced_quantity: parseInt(document.getElementById("c_produced_quantity").value) || 0,
  produced_date: document.getElementById("c_produced_date").value,
  shift: document.getElementById("c_shift").value,
  operator_id: document.getElementById("c_operator_id").value,
  };
  try {
    await axios.post(api, product_record);
    alert("✅ 新增成功");
  } catch (err) {
    alert("❌ 錯誤：" + (err.response?.data?.detail || err.message));
  }
}

async function readProduct_record() {
  const keyword = document.getElementById("r_keyword").value.toLowerCase();
  const res = await axios.get(api);
  const table = document.getElementById("readTable");
  table.innerHTML = "";
  res.data.forEach(f => {
    if (f.product_id.toString().includes(keyword)) {
      table.innerHTML += `<tr>
        <td>${f.record_id}</td><td>${f.line_id}</td>
        <td>${f.product_id}</td><td>${f.produced_quantity}</td>
        <td>${f.produced_date}</td><td>${f.shift}</td>
        <td>${f.operator_id}</td>
      </tr>`;
    }
  });
}

async function loadUpdateProduct_record() {
  const id = document.getElementById("u_id").value;
  try {
    const res = await axios.get(`${api}/${id}`);
    const f = res.data;
    document.getElementById("u_line_id").value = f.line_id;
    document.getElementById("u_product_id").value = f.product_id;
    document.getElementById("u_produced_quantity").value = f.produced_quantity;
    document.getElementById("u_produced_date").value = f.produced_date;
    document.getElementById("u_shift").value = f.shift;
    document.getElementById("u_operator_id").value = f.operator_id;
    document.getElementById("updateForm").style.display = "block";
  } catch (err) {
    alert("❌ 找不到工廠");
    document.getElementById("updateForm").style.display = "none";
  }
}

async function updateProduct_record() {
  const id = document.getElementById("u_id").value;
  const product_record = {
  line_id: document.getElementById("u_line_id").value,
  product_id: document.getElementById("u_product_id").value,
  produced_quantity: parseInt(document.getElementById("u_produced_quantity").value) || 0,
  produced_date: document.getElementById("u_produced_date").value,
  shift: document.getElementById("u_shift").value,
  operator_id: document.getElementById("u_operator_id").value,
  };
  try {
    await axios.put(`${api}/${id}`, product_record);
    alert("✅ 修改成功");
  } catch (err) {
    lert("❌ 修改失敗：" + err.message);
  }
}

async function deleteProduct_record() {
  const id = document.getElementById("d_id").value;
  if (!confirm(`確定要刪除工廠 ID ${id} 嗎？`)) return;
    try {
      await axios.delete(`${api}/${id}`);
      alert("✅ 刪除成功");
    } catch (err) {
      alert("❌ 刪除失敗：" + err.message);
    }
}
     