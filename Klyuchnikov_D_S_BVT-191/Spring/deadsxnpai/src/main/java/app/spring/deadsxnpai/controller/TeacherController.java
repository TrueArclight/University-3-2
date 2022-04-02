package app.spring.deadsxnpai.controller;

import app.spring.deadsxnpai.entity.TeacherEntity;
import app.spring.deadsxnpai.exceptions.TeacherNotFoundException;
import app.spring.deadsxnpai.service.TeacherService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/teachers")
public class TeacherController {
    @Autowired
    private TeacherService teacherService;
    @PostMapping
    public ResponseEntity insert(@RequestBody TeacherEntity teacherEntity,@RequestParam Long classId) {
        try {
            teacherService.createTeacher(teacherEntity, classId);
            return ResponseEntity.ok().body("Teacher added");
        } catch (Exception e) {
            return ResponseEntity.badRequest().body("Something went wrong\n" + e);
        }
    }
    @DeleteMapping("/{id}")
    public ResponseEntity deleteTeacher(@PathVariable long id){
        try {
            return ResponseEntity.ok().body(teacherService.deleteTeacher(id));
        } catch (Exception e) {
            return ResponseEntity.badRequest().body("Something went wrong");
        }
    }

    @GetMapping
    public ResponseEntity getOne(@RequestParam long id) {
        try {
            return ResponseEntity.ok().body(teacherService.getOne(id));
        } catch (TeacherNotFoundException e) {
            return ResponseEntity.badRequest().body(e.getMessage());
        } catch (Exception e) {
            return ResponseEntity.badRequest().body("Something went wrong");
        }
    }
}
