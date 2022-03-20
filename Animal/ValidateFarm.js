function checkId(id, length) {
  if ((id.length !== length) || !id.match(/^[0-9]+$/) {
    return "The id number must hold six digits.\n";
  }

  return "";
}

function checkName(name) {
  if (name.length == 0) {
    return "The name must not be empty.\n";
  }

  return "";
}

function checkAddress(address) {
  if (address.length == 0) {
    return "The address must not be empty.\n";
  }

  return "";
}

function checkPostal(postal) {
  if (postal.length == 0) {
    return "The postal address must not be empty.\n";
  }

  if (!registration.match(/^[0-9]+$/)) {
    return "The postal address must hold digits.\n";
  }  

  return "";
}


function checkPostal(postal) {
  if (postal.length == 0) {
    return "The phone number must not be empty.\n";
  }

  if (!registration.match(/^[0-9]+$/)) {
    return "The phone number must hold digits.\n";
  }  

  return "";
}
function validateFarm(idLength) {
  let result = checkId(document.getElementById("id").value, idLength);
  result += checkName(document.getElementById("name").value);
  result += checkAddress(document.getElementById("address").value);
  result += checkPostal(document.getElementById("postal").value);
  result += checkPhone(document.getElementById("phone").value);
  
  if (result.length > 0) {
    alert(result);
    return false;
  }

  document.getElementById("id").value = id.toUpperCase();
  return true;
}

/*console.log("checkPersonNumber(\"6822035953\") " + (checkPersonNumber("6822035953") ? "Yes" : "No"));
console.log("checkPersonNumber(\"6802315953\") " + (checkPersonNumber("6802315953") ? "Yes" : "No"));
console.log("checkPersonNumber(\"6802035953\") " + (checkPersonNumber("6802035953") ? "Yes" : "No"));
console.log("checkPersonNumber(\"6802035952\") " + (checkPersonNumber("6802035952") ? "Yes" : "No"));
console.log("checkPersonNumber(\"8112189876\") " + (checkPersonNumber("8112189876") ? "Yes" : "No"));
console.log("checkPersonNumber(\"8112189877\") " + (checkPersonNumber("8112189877") ? "Yes" : "No"));  
console.log("checkPersonNumber(\"1212121212\") " + (checkPersonNumber("1212121212") ? "Yes" : "No"));
console.log("checkPersonNumber(\"1212121213\") " + (checkPersonNumber("1212121213") ? "Yes" : "No"));

for (let index = 0; index < 100; ++index) {
  let personNumber = generatePersonNumber();
  //console.log(personNumber + " " + (checkPersonNumber(personNumber) ? "Yes" : "No"));
  document.write(personNumber + " " + (checkPersonNumber(personNumber) ? "Yes" : "No") + "<br>");
}

let personNumber = generatePersonNumber();
console.log(personNumber + " ");
console.log("Hello2");
console.log(checkPersonNumber(personNumber) ? "Yes" : "No");
console.log("Hello3");*/
