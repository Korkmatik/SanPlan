package com.korkmatik.sanplan.endpoints.api.v1;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController("/test")
public class TestEndpoint extends ApiV1Controller {

    @GetMapping
    public String test() {
        return "Hello";
    }
}
