<?php

namespace Bank\Models;

//use Bank\Domain\Bank;
use Bank\Exceptions\DbException;
use Bank\Exceptions\NotFoundException;
use PDO;

class OwnerModel extends AbstractModel {
  public function ownerList() {
    $ownerRows = $this->db->query("SELECT * FROM owner");
    if (!$ownerRows) die("Error owner List.");
      
    $ownerList = [];
    foreach ($ownerRows as $ownerRow) {
      $ownerId = htmlspecialchars($ownerRow["id"]);
      $ownerName = htmlspecialchars($ownerRow["name"]);
      $address = htmlspecialchars($ownerRow["address"]);
      $postal = htmlspecialchars($ownerRow["postal"]);
      $phone = htmlspecialchars($ownerRow["phone"]);

      $farmQuery = "SELECT * FROM farm INNER JOIN ownership " .
                   "ON (ownership.owner_id = :id) AND " .
                   "   (ownership.farm_id = farm.id);";
      $farmStatement = $this->db->prepare($farmQuery);
      $farmResult = $farmStatement->execute(["id" => $ownerId]);
      if (!$farmResult) die("Fatal error.");

      $oneOwner = 0;
      $farmList = [];
      while ($farmRow = $farmStatement->fetch()) {
        $farmId = htmlspecialchars($farmRow["id"]);
        $farmName = htmlspecialchars($farmRow["name"]);   
        $ownerIdList = $this->farmOwnerList($farmId);

        if ((count($ownerIdList) == 1) && ($ownerIdList[0] == $ownerId)) {
          $oneOwner = 1;
        }

        $sizeQuery = "SELECT * FROM ownership WHERE (farm_id = :farmId)";
        $sizeStatement = $this->db->prepare($sizeQuery);
        $sizeResult = $sizeStatement->execute(["farmId" => $farmId]);
        if (!$sizeResult) die("Fatal error.");
        $farmOneOwner = ($sizeStatement->rowCount() == 1);

        $farm = ["id" => $farmId, "name" => $farmName, 
                 "oneOwner" => $farmOneOwner];
        $farmList[] = $farm;
      }

      $owner = ["id" => $ownerId, "name" => $ownerName,
                "address" => $address, "postal" => $postal,
                "phone" => $phone, "farmList" => $farmList,
                "farmCount" => count($farmList), "oneOwner" => $oneOwner];
      $ownerList[] = $owner;
    }
    
    return $ownerList;
  }

  public function farmOwnerList($farmId) {
    $farmQuery = "SELECT * FROM owner INNER JOIN ownership" .
                  "  ON (:farmId = ownership.farm_id)" .
                  " AND (owner.id = ownership.owner_id)";
    $farmStatement = $this->db->prepare($farmQuery);
    $farmResult = $farmStatement->execute(["farmId" => $farmId]);
    if (!$farmResult) die($this->db->errorInfo()[2]);

    $ownerIdList = [];
    while ($ownerRow = $farmStatement->fetch()) {
      $ownerIdList[] = htmlspecialchars($ownerRow["id"]);
    }
    return $ownerIdList;
  }

  public function noFarmList($id) {
    $farmQuery = "SELECT * FROM farm INNER JOIN ownership".
                  "  ON (farm.id = ownership.farm_id)" .
                  " AND (ownership.owner_id = :id)";
    $farmStatement = $this->db->prepare($farmQuery);
    $farmResult = $farmStatement->execute(["id" => $id]);
    if (!$farmResult) die($this->db->errorInfo()[2]);

    $farmIdList = [];
    while ($farmRow = $farmStatement->fetch()) {
      $farmIdList[] = htmlspecialchars($farmRow["id"]);
    }
    
    $fullRows = $this->db->query("SELECT * FROM farm");
    if (!$fullRows) die("Error farm List.");
 
    $finalList = [];
    foreach ($fullRows as $fullRow) {
      $fullId = htmlspecialchars($fullRow["id"]);

      if (!(in_array($fullId, $farmIdList))) {
        $finalName = htmlspecialchars($fullRow["name"]);
        $final = ["id" => $fullId, "name" => $finalName];
        $finalList[] = $final;
      }
    }

    return $finalList;
  }

/*  public function farmList($id) {
    $farmRows = $this->db->query("SELECT * FROM farm");
    if (!$farmRows) die("Error farm List.");

    $farmList = [];
    foreach ($farmRows as $farmRow) {
      $farmId = htmlspecialchars($farmRow["id"]);
      $farmName = htmlspecialchars($farmRow["name"]);
      $farm = ["id" => $farmId, "name" => $farmName];
      $farmList[] = $farm;
    }

    return $farmList;
  }*/

  public function ownerAdd($id, $name, $address, $postal, $phone) {
    $ownerQuery = "SELECT * FROM owner WHERE (id = :id)";
    $ownerStatement = $this->db->prepare($ownerQuery);
    $ownerStatement->bindValue("id", $id, PDO::PARAM_STR);
    $ownerListResult = $ownerStatement->execute();
    if (!$ownerListResult) die($this->db->errorInfo()[2]);
    if ($ownerStatement->rowCount() > 0) {
      return false;
    }

    $ownerQuery = "INSERT INTO owner(id, name, address, postal, phone) " .
                      "VALUES(:id, :name, :address, :postal, :phone)";
    $ownerStatement = $this->db->prepare($ownerQuery);
    $ownerStatement->bindValue("id", $id, PDO::PARAM_STR);
    $ownerStatement->bindValue("name", $name, PDO::PARAM_STR);
    $ownerStatement->bindValue("address", $address, PDO::PARAM_STR);
    $ownerStatement->bindValue("postal", $postal, PDO::PARAM_STR);
    $ownerStatement->bindValue("phone", $phone, PDO::PARAM_STR);
    $result = $ownerStatement->execute();
    if (!$ownerStatement) die("Fatal error."); // $this->db->errorInfo());
    return true;
  }

  public function ownerEdit($id, $name, $address, $postal, $phone) {
    $ownerQuery = "UPDATE owner SET name = :name, address = :address, " .
                      "postal = :postal, phone = :phone where id = :id";
    $ownerStatement = $this->db->prepare($ownerQuery);
    $ownerStatement->bindValue("id", $id, PDO::PARAM_STR);
    $ownerStatement->bindValue("name", $name, PDO::PARAM_STR);
    $ownerStatement->bindValue("address", $address, PDO::PARAM_STR);
    $ownerStatement->bindValue("postal", $postal, PDO::PARAM_STR);
    $ownerStatement->bindValue("phone", $phone, PDO::PARAM_STR);
    $ownerStatement->execute();
    if (!$ownerStatement) die("Fatal error."); // $this->db->errorInfo());
  }

  public function ownerDelete($id) {
    $ownerQuery = "DELETE FROM ownership WHERE owner_id = :id";
    $ownerStatement = $this->db->prepare($ownerQuery);
    $ownerResult = $ownerStatement->execute(["id" => $id]);
    if (!$ownerResult) die($this->db->errorInfo()[2]);

    $ownerQuery = "DELETE FROM owner WHERE id = :id";
    $ownerStatement = $this->db->prepare($ownerQuery);
    $ownerResult = $ownerStatement->execute(["id" => $id]);
    if (!$ownerResult) die($this->db->errorInfo()[2]);
  }
  
  /*public function notFarmList($ownerId) {
    $farmQuery = "SELECT * FROM owner INNER JOIN ownership ON (ownership.farm_id != :farmId)";
    $farmStatement = $this->db->prepare($farmQuery);
    $farmStatement->bindValue("farmId", $farmId, PDO::PARAM_STR);
    $farmListResult = $farmStatement->execute();
    if (!$farmListResult) die($this->db->errorInfo()[2]);

    $farmList = [];
    while ($farmRow = $farmStatement->fetch()) {
      $farmId = htmlspecialchars($farmRow["id"]);
      $farmName = htmlspecialchars($farmRow["name"]);
      $farm = ["id" => $farmId, "name" => $farmName];
      $farmList[] = $farm;
    }
    return $farmList;
  }*/

  public function ownerAddFarm($ownerId, $farmId) {
    $ownerQuery = "SELECT * FROM ownership  WHERE (owner_id = :ownerId)" .
                      "                           AND (farm_id = :farmId)";
    $ownerStatement = $this->db->prepare($ownerQuery);
    $ownerStatement->bindValue("ownerId", $farmId, PDO::PARAM_STR);
    $ownerStatement->bindValue("farmId", $farmId, PDO::PARAM_STR);
    $ownerListResult = $ownerStatement->execute();
    if (!$ownerListResult) die($this->db->errorInfo()[2]);
    if ($ownerStatement->rowCount() > 0) {
      return false;
    }

    $ownerQuery = "INSERT INTO ownership(owner_id, farm_id)" .
                      "  VALUES(:ownerId, :farmId)";
    $ownerStatement = $this->db->prepare($ownerQuery);
    $ownerStatement->bindValue("ownerId", $ownerId, PDO::PARAM_STR);
    $ownerStatement->bindValue("farmId", $farmId, PDO::PARAM_STR);
    $ownerListResult = $ownerStatement->execute();
    if (!$ownerListResult) die($this->db->errorInfo()[2]);
    return true;
  }

  public function ownerRemoveFarm($ownerId, $farmId) {
    $ownerQuery = "SELECT * FROM ownership WHERE (farm_id = :farmId)";
    $ownerStatement = $this->db->prepare($ownerQuery);
    $ownerStatement->bindValue("farmId", $farmId, PDO::PARAM_STR);
    $ownerListResult = $ownerStatement->execute();
    if (!$ownerListResult) die($this->db->errorInfo()[2]);
    if ($ownerStatement->rowCount() == 1) {
      return false;
    }

    $ownerQuery = "DELETE FROM ownership" .
                  "  WHERE (owner_id = :ownerId) AND (farm_id = :farmId)";
    $ownerStatement = $this->db->prepare($ownerQuery);
    $ownerStatement->bindValue("ownerId", $ownerId, PDO::PARAM_STR);
    $ownerStatement->bindValue("farmId", $farmId, PDO::PARAM_STR);
    $ownerListResult = $ownerStatement->execute();
    if (!$ownerListResult) die($this->db->errorInfo()[2]);
    return true;
  }  
}