<?php
namespace Bank\Controllers;

use Bank\Exceptions\NotFoundException;
use Bank\Models\AnimalModel;

class AnimalController extends AbstractController {
  public function animalList() {
    $animalModel = new AnimalModel($this->db);
    $propertyMap = ["animalList" => $animalModel->animalList()];
    return $this->render("AnimalList.twig", $propertyMap);
  }

  public function animalAdd() {
    $animalModel = new AnimalModel($this->db);
    $propertyMap = ["kindList" => $animalModel->kindList(),
                    "farmList" => $animalModel->farmList()];
    return $this->render("AnimalAdd.twig", $propertyMap);
  }
    
  public function animalAdded() {
    $id = trim($this->request->getParams()->getString("id"));
    $name = trim($this->request->getParams()->getString("name"));

    $animalModel = new AnimalModel($this->db);
    $kindName = trim($this->request->getParams()->getString("kind"));
    $kindId = $animalModel->kindId($kindName);

    $farmText = trim($this->request->getParams()->getString("farm"));
    $spaceIndex = strpos($farmText, chr(194));
    $farmId = substr($farmText, 0, $spaceIndex);

    $ok = $animalModel->animalAdd($id, $kindId, $name, $farmId);
    $propertyMap = ["ok" => $ok, "id" => $id, "name" => $name,
                    "kindName" => $kindName, "farmText" => $farmText];
    return $this->render("AnimalAdded.twig", $propertyMap);
  }    

  public function animalEdit($animalId, $kindId, $name, $farmId) {
    $animalModel = new AnimalModel($this->db);
    $propertyMap = ["animalId" => $animalId, "kindId" => $kindId,
                    "name" => $name, "farmId" => $farmId,
                    "kindList" => $animalModel->kindList(),
                    "farmList" => $animalModel->farmList()];
    return $this->render("AnimalEdit.twig", $propertyMap);
  }
    
  public function animalEdited() {
    $animalId = trim($this->request->getParams()->getString("id"));
    $name = trim($this->request->getParams()->getString("name"));

    $kindName = trim($this->request->getParams()->getString("kind"));
    $animalModel = new AnimalModel($this->db);
    $kindId = $animalModel->kindId($kindName);

    $farmText = trim($this->request->getParams()->getString("farm"));
    $spaceIndex = strpos($farmText, chr(194));
    $farmId = substr($farmText, 0, $spaceIndex);
    $farmName = substr($farmText, $spaceIndex + 2);

    $animalModel->animalEdit($animalId, $kindId, $name, $farmId);
    $propertyMap = ["animalId" => $animalId, "kindName" => $kindName,
                    "name" => $name, "farmText" => $farmText];
    return $this->render("AnimalEdited.twig", $propertyMap);
  }    

  public function animalDelete($id, $name) {
    $animalModel = new AnimalModel($this->db);
    $animalModel->animalDelete($id);
    $propertyMap = ["id" => $id, "name" => $name];
    return $this->render("AnimalDeleted.twig", $propertyMap);
  }
}