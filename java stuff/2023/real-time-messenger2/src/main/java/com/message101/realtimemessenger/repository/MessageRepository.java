package com.message101.realtimemessenger.repository;

import org.springframework.data.mongodb.repository.MongoRepository;

import com.message101.realtimemessenger.model.Message;

public interface MessageRepository extends MongoRepository<Message, Integer>{

}
