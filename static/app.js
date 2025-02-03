const API_URL = "http://127.0.0.1:5000/api/cupcakes";

// handle form submission
$("#new-cupcake").on("submit", async function(e){
  e.preventDefault();
  
  let flavor = $("#form-flavor").val();
  let size = $("#form-size").val();
  let rating = $("#form-rating").val();
  let image = $("#form-image").val();

  const res = await axios.post(API_URL, {
    "flavor": flavor,
    "size": size,
    "rating": rating,
    "image": image
  });

  let cupcake = $(cupcakeHTML(res.data.cupcake));
  $("#cupcakes").append(cupcake);
  $("#new-cupcake").trigger("reset");
});


// handle X button click
$("#cupcakes").on("click", ".x-btn", async function(e){
  e.preventDefault();

  let $cupcake = $(e.target).closest("div");
  console.log("inside the delete");

  await axios.delete(`${API_URL}/${$cupcake.attr("data-id")}`);
  $cupcake.remove();
});

// create cupcake html
function cupcakeHTML(cupcake) {
  return `
  <div data-id="${cupcake.id}">
    <li>
      ${cupcake.flavor} | ${cupcake.size} | ${cupcake.rating}
      <button class="x-btn btn btn-danger btn-large">X</button>
    </li>
    <img style="width: 200px; height: 200px;" class="img-thumbnail"
      src="${cupcake.image}"
      alt="cupcake image">
  </div>`;
}

// put cupcakes on page
async function showCupcakes() {
  const res = await axios.get(API_URL);
  for (let cupcake of res.data.cupcakes) {
    let newCupcake = $(cupcakeHTML(cupcake));
    $("#cupcakes").append(newCupcake);
  }
}

$(showCupcakes());