# Week 1 Lecture Notes

## Session Title

Orientation, Ethics, HTTP Foundations, and Lab Setup

## Timing Plan

| Segment | Time | Focus |
| --- | ---: | --- |
| Welcome and course structure | 20 min | Expectations, schedule, grading, deliverables |
| Ethics and authorization | 35 min | Scope, permission, professional conduct |
| Break | 10 min |  |
| HTTP foundations | 45 min | Requests, responses, headers, cookies, methods, status codes |
| Trust boundaries and evidence | 35 min | User-controlled input, server trust, reporting evidence |
| Lab setup walkthrough | 25 min | Docker Compose, target URLs, troubleshooting |
| Discussion and wrap-up | 10 min | Questions and next steps |

## Instructor Preparation

- Confirm Docker images pull successfully before class.
- Have browser developer tools ready.
- Prepare a clean browser profile for demonstration.
- Decide whether students should use OWASP ZAP or Burp Suite for later labs.
- Prepare an example scope statement to show the class.

## Opening Message

This course teaches students to think like security engineers. Technical ability matters, but every technique sits inside authorization, scope, documentation, and responsible communication.

## Demonstration Flow

1. Open one local target, preferably OWASP Juice Shop.
2. Show the browser network panel.
3. Reload the page and identify the first document request.
4. Point out method, path, status code, selected headers, and cookies.
5. Explain what can and cannot be concluded from this baseline observation.
6. Show how to record evidence without copying unrelated data.

## Discussion Prompts

- What is the difference between curiosity and authorization?
- Why is a screenshot alone usually weak evidence?
- What makes a vulnerability report useful to an engineering team?
- Why can client-side validation be helpful but insufficient?

## Key Concepts to Emphasize

### Authorization

Testing without permission is not professional security work. Written scope protects the tester, the organization, and unrelated systems.

### HTTP State

HTTP itself does not remember users. Applications create state through cookies, sessions, tokens, local storage, server-side databases, and identity systems. Many serious vulnerabilities appear where state assumptions fail.

### Evidence

Evidence must support a specific claim. Students should learn early to capture the smallest useful proof and explain why it matters.

## Suggested Board Sketch

```text
Browser -> Request -> Web server -> App logic -> Database
Browser <- Response <- Web server <- App logic <- Database
```

Mark trust boundaries at the browser/server edge and application/database edge.

## Exit Ticket

Ask students to submit one sentence answering:

> What is one thing you are allowed to test in this course, and one thing you are not allowed to test?

## Textbook Reference

- [Chapter 1: Ethics, Authorization, and HTTP Foundations](../../textbook/chapters/01-ethics-authorization-and-http-foundations.md)
