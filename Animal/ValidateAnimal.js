function checkId(id, length) {
  if ((id.length !== length) || !id.match(/^[0-9]+$/) {
    return "The id number must hold six digits.\n";
  }

  return "";
}

function checkKind(kind) {
  if (kind.length == 0) {
    return "The kind must chosen.\n";
  }

  return "";
}

function checkName(name) {
  if (name.length == 0) {
    return "The name must not be empty.\n";
  }

  return "";
}

function validateAnimal(idLength) {
  alert("Hello");
  let result = checkId(document.getElementById("id").value, idLength);
  result += checkKind(document.getElementById("kind").value);
  result += checkName(document.getElementById("name").value);
  
  if (result.length > 0) {
    alert(result);
    return false;
  }

  document.getElementById("id").value = id.toUpperCase();
  return true;
}
