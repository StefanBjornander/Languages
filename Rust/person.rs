struct Person {
  name : String
}

impl Person {
  fn get_name(self) -> String {
    self.name
  }

  /*fn to_String(self) -> String {
    self.name
  }*/
}

fn main() {
  let p = Person{name: "Adam".to_string()};
  //println!("Person: {}", p.to_string());
  println!("Name: {}", p.get_name());
}