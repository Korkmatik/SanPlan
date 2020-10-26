package local.korkmatik.SanPlan.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.stereotype.Repository;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class AuthenticationController {

    @GetMapping("/")
    public String home() {
        return "Home page";
    }

    @GetMapping("/login")
    public String login() {
        return "login.html";
    }

    @GetMapping("/access-denied")
    public String accessDenied() {
        return "/error/access-denied";
    }
}
