const api = "http://localhost:8000/products";

function switchMode() {
  document.querySelectorAll(".crud-box").forEach(box => box.style.display = "none");
  const mode = document.getElementById("crudSelect").value;
  if (mode) document.getElementById(mode + "Box").style.display = "block";
}

async function createProduct() {
  const product = {
    name: document.getElementById("c_name").value,
    catagory: document.getElementById("c_catagory").value,
    price: document.getElementById("c_price").value,
    spec: document.getElementById("c_spec").value,
  };
  try {
    await axios.post(api, product);
    alert("✅ 新增成功");
  } catch (err) {
    alert("❌ 錯誤：" + (err.response?.data?.detail || err.message));
  }
}

async function readProduct() {
  const keyword = document.getElementById("r_keyword").value.toLowerCase();
  const res = await axios.get(api);
  const table = document.getElementById("readTable");
  table.innerHTML = "";
  res.data.forEach(f => {
  if (f.name.toLowerCase().includes(keyword)) {
    table.innerHTML += `<tr>
      <td>${f.product_id}</td><td>${f.name}</td>
      <td>${f.category}</td><td>${f.price}</td>
      <td>${f.spec}</td>
    </tr>`;
    }
  });
}

async function loadUpdateProduct() {
  const id = document.getElementById("u_id").value;
  try {
    const res = await axios.get(`${api}/${id}`);
    const f = res.data;
    document.getElementById("u_name").value = f.name;
    document.getElementById("u_catagory").value = f.catagory;
    document.getElementById("u_price").value = f.price;
    document.getElementById("u_spec").value = f.spec;
    document.getElementById("updateForm").style.display = "block";
  } catch (err) {
    alert("❌ 找不到工廠");
    document.getElementById("updateForm").style.display = "none";
  }
}

async function updateProduct() {
  const id = document.getElementById("u_id").value;
  const product = {
    name: document.getElementById("u_name").value,
    catagory: document.getElementById("u_catagory").value,
    price: document.getElementById("u_price").value,
    spec: document.getElementById("u_spec").value,
  };
  try {
    await axios.put(`${api}/${id}`, product);
    alert("✅ 修改成功");
  } catch (err) {
    alert("❌ 修改失敗：" + err.message);
  }
}


async function deleteProduct() {
  const id = document.getElementById("d_id").value;
  if (!confirm(`確定要刪除工廠 ID ${id} 嗎？`)) return;
    try {
      await axios.delete(`${api}/${id}`);
      alert("✅ 刪除成功");
    } catch (err) {
      alert("❌ 刪除失敗：" + err.message);
  }
}
