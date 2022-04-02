package app.spring.deadsxnpai.controller;


import app.spring.deadsxnpai.entity.StudentEntity;
import app.spring.deadsxnpai.exceptions.StudentNotFoundException;
import app.spring.deadsxnpai.service.ClassService;
import app.spring.deadsxnpai.service.StudentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/students")
public class StudentController {

    @Autowired
    private StudentService studentService;
    @Autowired
    private ClassService classService;

    @PostMapping
    public ResponseEntity create(@RequestBody StudentEntity student, @RequestParam long classId) {
        try {
            studentService.createStudent(student,classId);
            return ResponseEntity.ok().body("Student added");
        } catch (Exception e) {
            return ResponseEntity.badRequest().body("Something went wrong\n" + e);
        }
    }

    @GetMapping
    public ResponseEntity getOne(@RequestParam long id) {
        try {
            return ResponseEntity.ok().body(studentService.getOne(id));
        } catch (StudentNotFoundException e) {
            return ResponseEntity.badRequest().body(e.getMessage());
        } catch (Exception e) {
            return ResponseEntity.badRequest().body("Something went wrong");
        }
    }
    @DeleteMapping("/{id}")
    public ResponseEntity deleteStudent(@PathVariable long id){
        try {
            return ResponseEntity.ok().body(studentService.deleteStudent(id));
        } catch (Exception e) {
            return ResponseEntity.badRequest().body("Something went wrong");
        }
    }

    /*@PutMapping
    public ResponseEntity addClass(@RequestParam long id){
        try{

        }catch (Exception e){

        }
    }*/
}
