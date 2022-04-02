package app.spring.deadsxnpai.controller;

import app.spring.deadsxnpai.entity.ClassEntity;
import app.spring.deadsxnpai.exceptions.CodeAlreadyExist;
import app.spring.deadsxnpai.exceptions.CodeNotFoundException;
import app.spring.deadsxnpai.service.ClassService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/class")
public class ClassController {

    @Autowired
    private ClassService classService;
    @PostMapping
    public ResponseEntity createClass(@RequestBody ClassEntity classEntity) {
        try {
            classService.createClass(classEntity);
            return ResponseEntity.ok().body("Class added");
        } catch (CodeAlreadyExist e) {
            return ResponseEntity.badRequest().body("Code exception\n" + e);
        } catch (Exception e) {
            return ResponseEntity.badRequest().body("Something went wrong\n" + e);
        }
    }
    @DeleteMapping("/{id}")
    public ResponseEntity deleteClass(@PathVariable long id){
        try {
            return ResponseEntity.ok().body(classService.deleteClass(id));
        } catch (Exception e) {
            return ResponseEntity.badRequest().body("Something went wrong");
        }
    }

    @GetMapping
    public ResponseEntity getOne(@RequestParam long id) {
        try {
            return ResponseEntity.ok().body(classService.getOne(id));
        } catch (CodeNotFoundException e) {
            return ResponseEntity.badRequest().body(e.getMessage());
        } catch (Exception e) {
            return ResponseEntity.badRequest().body("Something went wrong");
        }
    }


}
