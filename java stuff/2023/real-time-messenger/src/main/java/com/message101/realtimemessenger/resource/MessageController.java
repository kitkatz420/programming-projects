package com.message101.realtimemessenger.resource;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.message101.realtimemessenger.model.Message;
import com.message101.realtimemessenger.repository.MessageRepository;

@RestController
public class MessageController {

    @Autowired
    private MessageRepository repository;

    @PostMapping("/addMessage")
    public String saveMessage(@RequestBody Message message) {
        repository.save(message);
        return "Added message with id : " + message.getId();
    }

    @GetMapping("/findAllMessages")
    public List<Message> getMessage() {
        return repository.findAll();
    }

    @GetMapping("/findAllMessages/{id}")
    public Optional<Message> getMessage(@PathVariable int id) {
        return repository.findById(id);
    }

    @DeleteMapping("/delete/{id}")
    public String deleteMessage(@PathVariable int id) {
        repository.deleteById(id);
        return "Message deleted with id : " + id;
    }

}
