const gridBtn = document.getElementById("grid");
const columnBtn = document.getElementById("column");

let products = document.querySelectorAll(".product_item");

gridBtn.addEventListener("click", ()=>{
    products.forEach(product =>{
        if(product.classList.contains("col-xl-6")){
            product.classList.remove("col-xl-6");
        }
    });
})

columnBtn.addEventListener("click", ()=>{
    products.forEach(product =>{
        if(!product.classList.contains("col-xl-6")){
            product.classList.add("col-xl-6");
        }
    });
})