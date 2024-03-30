package com.message101.realtimemessenger.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@Getter
@Setter
@ToString

@Document(collection = "Message")
public class Message {
    @Id
    private int id;
    private String messageContent;
    private String userName;
}
