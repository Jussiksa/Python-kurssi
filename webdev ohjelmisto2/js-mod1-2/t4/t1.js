// querySelector valitsee aina yhden löydetyn elementin, jos useita
const output = document.querySelector("#output");
output.textContent = "Skripti käynnissä.";

// 1. haetaan uusi taulukon perusteella ja lisätään HTML:ää
const inventoryList = document.querySelector("#inventory > ol");
inventoryList.innerHTML = "<li>Miekka</li><li>Kilpi</li><li>Portteri</li>";

// 2. haetaan div-elementti CSS-selektorilla
const inventoryDiv = document.querySelector("#inventory");

// 3. haetaan divin sisällä oleva ul-elementti
const inventoryListUl = inventoryDiv.querySelector("ul");

// 4. luodaan uusi li-tunnistus listalle
// Esimerkki: inventoryListUl.innerHTML += "<li>Uusi tavara</li>";

// 5. haetaan inventoryItems.length ja...
// const itemsLength = inventoryItems.length;

// const "string", tommI;
// Esimerkki generoidusta HTML:stä elementin sisään:
// inventoryDiv.innerHTML = "<p>Uusi</p>";