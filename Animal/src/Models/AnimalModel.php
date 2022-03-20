<?php
namespace Bank\Models;

//use Bank\Domain\Bank;
use Bank\Exceptions\DbException;
use Bank\Exceptions\NotFoundException;
use PDO;

class AnimalModel extends AbstractModel {
  public function animalList() {
    $kindRows = $this->db->query("SELECT * FROM kind");
    if (!$kindRows) die("Error animal List.");

    $kindMap = [];
    foreach ($kindRows as $kindRow) {
      $kindMap[$kindRow["id"]] = $kindRow["name"];
    }

    $animalRows = $this->db->query("SELECT * FROM animal");
    if (!$animalRows) die("Error animal List.");
      
    $animalList = [];
    foreach ($animalRows as $animalRow) {
      $animalId = htmlspecialchars($animalRow["animal_id"]);
      $kindId = htmlspecialchars($animalRow["kind_id"]);
      $kindName = $kindMap[$kindId];
      $animalName = htmlspecialchars($animalRow["name"]);
      $farmId = htmlspecialchars($animalRow["farm_id"]);

      $farmQuery = "SELECT name FROM farm WHERE (id = :id)";
      $farmStatement = $this->db->prepare($farmQuery);
      $farmResult = $farmStatement->execute(["id" => $farmId]);
      if (!$farmResult) die("Fatal error.");
      $farmRow = $farmStatement->fetch();
      $farmName = htmlspecialchars($farmRow["name"]);

      $animal = ["id" => $animalId, "kindId" => $kindId,
                 "kindName" => $kindName, "name" => $animalName,
                 "farmId" => $farmId, "farmName" => $farmName];
      $animalList[] = $animal;
    }
    
    return $animalList;
  }

  public function kindList() {
    $kindRows = $this->db->query("SELECT * FROM kind");
    if (!$kindRows) die("Error kind List.");

    $kindList = [];
    foreach ($kindRows as $kindRow) {
      $kind = ["id" => $kindRow["id"], "name" => $kindRow["name"]];
      $kindList[] = $kind;
    }

    return $kindList;
  }

  public function kindName($id) {
    $kindQuery = "SELECT name FROM kind WHERE (id = :id)";
    $kindStatement = $this->db->prepare($kindQuery);
    $kindResult = $kindStatement->execute(["id" => $id]);
    if (!$kindResult) die($this->db->errorInfo()[2]);
    $kindRow = $kindStatement->fetch();
    var_dump($kindRow);
    return htmlspecialchars($kindRow["name"]);
  }

  public function kindId($name) {
    $kindQuery = "SELECT id FROM kind WHERE (name = :name)";
    $kindStatement = $this->db->prepare($kindQuery);
    $kindResult = $kindStatement->execute(["name" => $name]);
    if (!$kindResult) die($this->db->errorInfo()[2]);
    $kindRow = $kindStatement->fetch();
    return htmlspecialchars($kindRow["id"]);
  }

  /*private function kindMap() {
    $kindRows = $this->db->query("SELECT * FROM kind");
    if (!$kindRows) die("Error kind List.");

    $kindMap = [];
    foreach ($kindRows as $kindRow) {
      $kindMap[$kindRow["name"]] = $kindRow["id"];
    }
    return $kindMap;
  }*/

  public function farmList() {
    $farmRows = $this->db->query("SELECT * FROM farm");
    if (!$farmRows) die("Error farm List.");
      
    $farmList = [];
    foreach ($farmRows as $farmRow) {
      $farmId = htmlspecialchars($farmRow["id"]);
      $farmName = htmlspecialchars($farmRow["name"]);
      $farmList[] = ["id" => $farmId, "name" => $farmName];
    }
    return $farmList;
  }

  public function animalAdd($animalId, $kindId, $animalName, $farmId) {
    $animalQuery = "SELECT * FROM animal WHERE (animal_id = :animalId)";
    $animalStatement = $this->db->prepare($animalQuery);
    $animalResult = $animalStatement->execute(["animalId" => $animalId]);
    if (!$animalResult) die($this->db->errorInfo()[2]);
    $rowCount = $animalStatement->rowCount();
    if ($rowCount > 0) {
      return false;
    }

    $animalQuery = "INSERT INTO animal(animal_id, kind_id, name, farm_id)" .
                   "  VALUES(:animalId, :kindId, :name, :farmId)";
    $animalStatement = $this->db->prepare($animalQuery);
    $animalStatement->bindValue("animalId", $animalId, PDO::PARAM_STR);
    $animalStatement->bindValue("kindId", $kindId, PDO::PARAM_INT);
    $animalStatement->bindValue("name", $animalName, PDO::PARAM_STR);
    $animalStatement->bindValue("farmId", $farmId, PDO::PARAM_STR);
    $result = $animalStatement->execute();
    if (!$animalStatement) die("Fatal error."); // $this->db->errorInfo());
    return true;
  }

  public function animalEdit($animalId, $kindId, $name, $farmId) {
    $animalQuery = "UPDATE animal SET kind_id = :kindId, name = :name," .
                   "farm_id = :farmId WHERE (animal_id = :animalId)";
    $animalStatement = $this->db->prepare($animalQuery);
    $animalStatement->bindValue("kindId", $kindId, PDO::PARAM_INT);
    $animalStatement->bindValue("name", $name, PDO::PARAM_STR);
    $animalStatement->bindValue("farmId", $farmId, PDO::PARAM_STR);
    $animalStatement->bindValue("animalId", $animalId, PDO::PARAM_STR);
    $animalStatement->execute();
    if (!$animalStatement) die("Fatal error."); // $this->db->errorInfo());
  }

  public function animalDelete($id) {
    $animalQuery = "DELETE FROM animal WHERE animal_id = :id";
    $animalStatement = $this->db->prepare($animalQuery);
    $animalStatement->bindValue("id", $id, PDO::PARAM_STR);
    $animalResult = $animalStatement->execute();
    if (!$animalResult) die($this->db->errorInfo()[2]);
  }
}