<?php

namespace Bank\Models;

//use Bank\Domain\Bank;
use Bank\Exceptions\DbException;
use Bank\Exceptions\NotFoundException;
use PDO;

class FarmModel extends AbstractModel {
  public function farmList() {
    $farmRows = $this->db->query("SELECT * FROM farm");
    if (!$farmRows) die("Error farm List.");
      
    $farmList = [];
    foreach ($farmRows as $farmRow) {
      $farmId = htmlspecialchars($farmRow["id"]);
      $farmName = htmlspecialchars($farmRow["name"]);
      $address = htmlspecialchars($farmRow["address"]);
      $postal = htmlspecialchars($farmRow["postal"]);
      $phone = htmlspecialchars($farmRow["phone"]);

      $ownerQuery = "SELECT * FROM owner INNER JOIN ownership " .
                    "ON (ownership.farm_id = :id) AND " .
                    "   (ownership.owner_id = owner.id);";
      $ownerStatement = $this->db->prepare($ownerQuery);
      $ownerResult = $ownerStatement->execute(["id" => $farmId]);
      if (!$ownerResult) die("Fatal error.");

      $ownerList = [];
      while ($ownerRow = $ownerStatement->fetch()) {
        $ownerId = htmlspecialchars($ownerRow["id"]);
        $ownerName = htmlspecialchars($ownerRow["name"]);
        $owner = ["id" => $ownerId, "name" => $ownerName];
        $ownerList[] = $owner;
      }

      $animalQuery = "SELECT * FROM animal WHERE (farm_id = :id)";
      $animalStatement = $this->db->prepare($animalQuery);
      $animalResult = $animalStatement->execute(["id" => $farmId]);
      if (!$animalResult) die("Fatal error.");

      $kindRows = $this->db->query("SELECT * FROM kind");
      if (!$kindRows) die("Error animal List.");

      $kindMap = [];
      foreach ($kindRows as $kindRow) {
        $kindMap[$kindRow["id"]] = $kindRow["name"];
      }

      $animalList = [];
      while ($animalRow = $animalStatement->fetch()) {
        $animalId = htmlspecialchars($animalRow["animal_id"]);
        $kindId = htmlspecialchars($animalRow["kind_id"]);
        $kindName = $kindMap[$kindId];
        $animalName = htmlspecialchars($animalRow["name"]);
        $animal = ["id" => $animalId, "kind" => $kindName,
                   "name" => $animalName];
        $animalList[] = $animal;
      }

      $farm = ["id" => $farmId, "name" => $farmName,
               "address" => $address, "postal" => $postal,
               "phone" => $phone, "ownerList" => $ownerList,
               "ownerCount" => count($ownerList),
               "animalList" => $animalList,
               "animalCount" => count($animalList)];
      $farmList[] = $farm;
    }
    
    return $farmList;
  }

  public function noOwnerList($id) {
    $ownerQuery = "SELECT * FROM owner INNER JOIN ownership".
                  "  ON (owner.id = ownership.owner_id)" .
                  " AND (ownership.farm_id = :id)";
    $ownerStatement = $this->db->prepare($ownerQuery);
    $ownerResult = $ownerStatement->execute(["id" => $id]);
    if (!$ownerResult) die($this->db->errorInfo()[2]);

    $ownerIdList = [];
    while ($ownerRow = $ownerStatement->fetch()) {
      $ownerIdList[] = htmlspecialchars($ownerRow["id"]);
    }

    $fullRows = $this->db->query("SELECT * FROM owner");
    if (!$fullRows) die("Error farm List.");
      
    $finalList = [];
    foreach ($fullRows as $fullRow) {
      $fullId = htmlspecialchars($fullRow["id"]);

      if (!(in_array($fullId, $ownerIdList))) {
        $finalName = htmlspecialchars($fullRow["name"]);
        $final = ["id" => $fullId, "name" => $finalName];
        $finalList[] = $final;
      }
    }

    return $finalList;
  }

  public function farmAdd($id, $name, $address, $postal, $phone) {
    $ownerListQuery = "SELECT * FROM farm WHERE (id = :id)";
    $ownerStatement = $this->db->prepare($ownerListQuery);
    $ownerStatement->bindValue("id", $id, PDO::PARAM_STR);
    $ownerListResult = $ownerStatement->execute();
    if (!$ownerListResult) die($this->db->errorInfo()[2]);
    if ($ownerStatement->rowCount() > 0) {
      return false;
    }

    $farmListQuery = "INSERT INTO farm(id, name, address, postal, phone) " .
                     "VALUES(:id, :name, :address, :postal, :phone)";
    $farmStatement = $this->db->prepare($farmListQuery);
    $farmStatement->bindValue("id", $id, PDO::PARAM_STR);
    $farmStatement->bindValue("name", $name, PDO::PARAM_STR);
    $farmStatement->bindValue("address", $address, PDO::PARAM_STR);
    $farmStatement->bindValue("postal", $postal, PDO::PARAM_STR);
    $farmStatement->bindValue("phone", $phone, PDO::PARAM_STR);
    $result = $farmStatement->execute();
    if (!$farmStatement) die("Fatal error."); // $this->db->errorInfo());
    return $result;
  }

  public function farmEdit($id, $name, $address, $postal, $phone) {
    $farmListQuery = "UPDATE farm SET name = :name, address = :address, " .
                   "postal = :postal, phone = :phone where id = :id";
    $farmStatement = $this->db->prepare($farmListQuery);
    $farmStatement->bindValue("id", $id, PDO::PARAM_STR);
    $farmStatement->bindValue("name", $name, PDO::PARAM_STR);
    $farmStatement->bindValue("address", $address, PDO::PARAM_STR);
    $farmStatement->bindValue("postal", $postal, PDO::PARAM_STR);
    $farmStatement->bindValue("phone", $phone, PDO::PARAM_STR);
    $farmStatement->execute();
    if (!$farmStatement) die("Fatal error."); // $this->db->errorInfo());
  }

  public function farmDelete($id) {
    /*$ownerListQuery = "SELECT FROM animals WHERE (farm_id = :id)";
    $ownerStatement = $this->db->prepare($ownerListQuery);
    $ownerStatement->bindValue("id", $id, PDO::PARAM_STR);
    $ownerListResult = $ownerStatement->execute();
    if (!$ownerListResult) die($this->db->errorInfo()[2]);
    
    $animalCount = $ownerStatement->rowCount();
    if ($animalCount > 0) {
      return $animalCount;
    }*/

    $farmQuery = "DELETE FROM ownership WHERE farm_id = :id";
    $farmStatement = $this->db->prepare($farmQuery);
    $farmResult = $farmStatement->execute(["id" => $id]);
    if (!$farmResult) die($this->db->errorInfo()[2]);

    $farmListQuery = "DELETE FROM farm WHERE id = :id";
    $farmStatement = $this->db->prepare($farmListQuery);
    $farmListResult = $farmStatement->execute(["id" => $id]);
    if (!$farmListResult) die($this->db->errorInfo()[2]);
    //return 0;
  }

  /*public function notOwnerList($farmId) {
    $ownerListQuery = "SELECT * FROM owner INNER JOIN ownership ON (ownership.farm_id != :farmId)";
    $ownerStatement = $this->db->prepare($ownerListQuery);
    $ownerStatement->bindValue("farmId", $farmId, PDO::PARAM_STR);
    $ownerListResult = $ownerStatement->execute();
    if (!$ownerListResult) die($this->db->errorInfo()[2]);

    $ownerList = [];
    while ($ownerRow = $ownerStatement->fetch()) {
      $ownerId = htmlspecialchars($ownerRow["id"]);
      $ownerName = htmlspecialchars($ownerRow["name"]);
      $owner = ["id" => $ownerId, "name" => $ownerName];
      $ownerList[] = $owner;
    }
    return $ownerList;
  }*/
}