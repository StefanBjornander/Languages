function validate(length) {
  let result = checkId(document.getElementById("id").value, length);
  result += checkKind(document.getElementById("kind").value);
  result += checkName(document.getElementById("name").value);
  result += checkFarm(document.getElementById("farm").value);

  if (result.length > 0) {
    alert(result);
    return false;
  }

  return true;
}

function checkId(id, length) {
  if ((id.length !== length) || !id.match(/^[0-9]+$/)) {
    return "The identity number must hold 10 digits.\n";
  }

  return "";
}

function checkKind(kind) {
  if (kind.length == 0) {
    return "You have to select a kind.\n";
  }

  return "";
}

function checkName(name) {
  if (name.length == 0) {
    return "You have to input a name.\n";
  }

  return "";
}

function checkFarm(farm) {
  if (farm.length == 0) {
    return "You have to select a farm.\n";
  }

  return "";
}
