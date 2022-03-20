<?php
namespace Bank\Controllers;

use Bank\Exceptions\NotFoundException;
use Bank\Models\OwnerModel;

class OwnerController extends AbstractController {
  public function ownerList() {
    $ownerModel = new OwnerModel($this->db);
    $propertyMap = ["ownerList" => $ownerModel->ownerList()];
    return $this->render("OwnerList.twig", $propertyMap);
  }

  public function ownerAdd() {
    return $this->render("OwnerAdd.twig", []);
  }
    
  public function ownerAdded() {
    $id = trim($this->request->getParams()->getString("id"));
    $name = trim($this->request->getParams()->getString("name"));
    $address = trim($this->request->getParams()->getString("address"));
    $postal = trim($this->request->getParams()->getString("postal"));
    $phone = trim($this->request->getParams()->getString("phone"));
    $ownerModel = new OwnerModel($this->db);
    $ok = $ownerModel->ownerAdd($id, $name, $address, $postal, $phone);
    $propertyMap = ["ok" => $ok, "id" => $id, "name" => $name,
                    "address" => $address, "postal" => $postal,
                    "phone" => $phone];
    return $this->render("OwnerAdded.twig", $propertyMap);
  }    

  public function ownerEdit($id, $name, $address, $postal, $phone) {
    $propertyMap = ["id" => $id, "name" => $name, "address" => $address,
                    "postal" => $postal, "phone" => $phone];
    return $this->render("OwnerEdit.twig", $propertyMap);
  }
    
  public function ownerEdited() {
    $id = trim($this->request->getParams()->getString("id"));
    $name = trim($this->request->getParams()->getString("name"));
    $address = trim($this->request->getParams()->getString("address"));
    $postal = trim($this->request->getParams()->getString("postal"));
    $phone = trim($this->request->getParams()->getString("phone"));
    $ownerModel = new OwnerModel($this->db);
    $ownerModel->ownerEdit($id, $name, $address, $postal, $phone);
    $propertyMap = ["id" => $id, "name" => $name, "address" => $address,
                    "postal" => $postal, "phone" => $phone];
    return $this->render("OwnerEdited.twig", $propertyMap);
  }    

  public function ownerDeleted($id, $name) {
    $ownerModel = new OwnerModel($this->db);
    $ownerModel->ownerDelete($id);
    $propertyMap = ["id" => $id, "name" => $name];
    return $this->render("OwnerDeleted.twig", $propertyMap);
  }

  public function ownerAddFarm($id, $name) {
    $ownerModel = new OwnerModel($this->db);
    $noFarmList = $ownerModel->noFarmList($id);
    $propertyMap = ["id" => $id, "name" => $name,
                    "noFarmList" => $noFarmList];
    return $this->render("OwnerAddFarm.twig", $propertyMap);
  }

  public function ownerAddedFarm($ownerId, $ownerName) {
    $farmText = trim($this->request->getParams()->getString("farm"));
    $spaceIndex = strpos($farmText, chr(194));
    $farmId = substr($farmText, 0, $spaceIndex);
    $farmName = substr($farmText, $spaceIndex + 2);

    $ownerModel = new OwnerModel($this->db);
    $ok = $ownerModel->ownerAddFarm($ownerId, $farmId);
    $propertyMap = ["ok" => $ok, "ownerName" => $ownerName, "farmName" => $farmName];
    return $this->render("OwnerAddedFarm.twig", $propertyMap);
  }

  public function ownerRemovedFarm($ownerId, $ownerName, $farmId, $farmName) {
    $ownerModel = new OwnerModel($this->db);
    $ownerModel->ownerRemoveFarm($ownerId, $farmId);
    $propertyMap = ["ownerName" => $ownerName, "farmName" => $farmName];
    return $this->render("ownerRemovedFarm.twig", $propertyMap);
  }
}