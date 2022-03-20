<?php
namespace Bank\Controllers;

use Bank\Exceptions\NotFoundException;
use Bank\Models\FarmModel;
use Bank\Models\OwnerModel;

class FarmController extends AbstractController {
  public function farmList() {
    $farmModel = new FarmModel($this->db);
    $propertyMap = ["farmList" => $farmModel->farmList()];
    return $this->render("FarmList.twig", $propertyMap);
  }

  public function farmAdd() {
    return $this->render("FarmAdd.twig", []);
  }
    
  public function animalAdd() {
    $kindModel = new AnimalModel($this->db);
    $propertyMap = ["kindList" => $kindModel->kindList()];
    return $this->render("AnimalAdd.twig", $propertyMap);
  }
    
  public function farmAdded() {
    $id = trim($this->request->getParams()->getString("id"));
    $name = trim($this->request->getParams()->getString("name"));
    $address = trim($this->request->getParams()->getString("address"));
    $postal = trim($this->request->getParams()->getString("postal"));
    $phone = trim($this->request->getParams()->getString("phone"));
    $farmModel = new FarmModel($this->db);
    $ok = $farmModel->farmAdd($id, $name, $address, $postal, $phone);
    $propertyMap = ["ok" => $ok, "id" => $id, "name" => $name,
                    "address" => $address, "postal" => $postal,
                    "phone" => $phone];
    return $this->render("FarmAdded.twig", $propertyMap);
  }    

  public function farmEdit($id, $name, $address, $postal, $phone) {
    $propertyMap = ["id" => $id, "name" => $name, "address" => $address,
                    "postal" => $postal, "phone" => $phone];
    return $this->render("FarmEdit.twig", $propertyMap);
  }
    
  public function farmEdited() {
    $id = trim($this->request->getParams()->getString("id"));
    $name = trim($this->request->getParams()->getString("name"));
    $address = trim($this->request->getParams()->getString("address"));
    $postal = trim($this->request->getParams()->getString("postal"));
    $phone = trim($this->request->getParams()->getString("phone"));
    $farmModel = new FarmModel($this->db);
    $farmModel->farmEdit($id, $name, $address, $postal, $phone);
    $propertyMap = ["id" => $id, "name" => $name, "address" => $address,
                    "postal" => $postal, "phone" => $phone];
    return $this->render("FarmEdited.twig", $propertyMap);
  }    

  public function farmDeleted($id, $name) {
    $farmModel = new FarmModel($this->db);
    $farmModel->farmDelete($id);
    $propertyMap = ["name" => $name];
    return $this->render("FarmDeleted.twig", $propertyMap);
  }

  public function farmAddOwner($id, $name) {
    $farmModel = new FarmModel($this->db);
    $noOwnerList = $farmModel->noOwnerList($id);
    $propertyMap = ["id" => $id, "name" => $name,
                    "noOwnerList" => $noOwnerList];
    return $this->render("FarmAddOwner.twig", $propertyMap);
  }

  public function farmAddedOwner($farmId, $farmName) {
    $ownerText = trim($this->request->getParams()->getString("owner"));
    $spaceIndex = strpos($ownerText, chr(194));
    $ownerId = substr($ownerText, 0, $spaceIndex);
    $ownerName = substr($ownerText, $spaceIndex + 2);
    $ownerModel = new OwnerModel($this->db);
    $ownerModel->ownerAddFarm($ownerId, $farmId);
    $propertyMap = ["farmName" => $farmName, "ownerName" => $ownerName];
    return $this->render("FarmAddedOwner.twig", $propertyMap);
  }

  public function farmRemovedOwner($farmId, $farmName, $ownerId, $ownerName) {
    $ownerModel = new OwnerModel($this->db);
    $ok = $ownerModel->ownerRemoveFarm($ownerId, $farmId);
    $propertyMap = ["ok" => $ok, "ownerName" => $ownerName,
                    "farmName" => $farmName];
    return $this->render("FarmRemovedOwner.twig", $propertyMap);
  }
}