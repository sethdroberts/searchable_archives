# Agile Breakdown of App Development

## App Concept
Give historical researchers the ability to search text in poorly-scanned historical documents (e.g. half-faded, multi-column layouts). 

The app must accurately capture all the text in the document (even if poorly preserved) and output the same document with searchable text (either through layering or re-embedding) so the user can search the *original* document.

## Persona

### Bio:
Title: Theology/History PhD Student
Name: James Manchester
32 years old
Male
Married
Has an MA in Theology from AU/SAU
Completing a Theology PhD

James is a hard-working theology student at Andrews University.

### Goals:
- Read/review through thousands of historical documents
- Write a dissertation that is historically rigorous and accurate
- Spend time with family

### Tasks:
- Spend lots of time reading
- Search and parse through hundreds of thousands of documents searching for relevant material
- Compile and annotate relevant quotes and historical documents
- Write up a cohesive dissertation while keeping all documents straight

### Tech Background:
James is not very adept at technology. He knows how to check email, do searches in archives, etc., but is completely unfamiliar with software engineering or anything more complicated than Scrivener.

### Environment:
He owns a Mac and an iPhone, but does his main research work on his Mac with either built-in tools or web ones.

## Scenarios

### Scenario 1:
Found a document that's important, but it's hard to see exactly what the text is saying. He uploads it into the app so he can see the reconstructed version of the text he's missing (an on-off toggle might be helpful, if there's not a way to reconstuct that in an output PDF).

### Scenario 2:
Found a long document that he needs to go through to see if there's anything useful in it, but because it's not searchable, he has to manually read through the entire thing. So he uploads it to the app, and it outputs a PDF he can easily search for keywords in.

### Scenario 3:
Found a searchable old document, but it's been processed by an OCR that is inaccurate, so it's difficult to search for specific terms. He knows there's a specific quote there, but can't find it via search. So he uploads it to the app, and it outputs an OCR version that's far more accurate, and also reconstructs missing words and sentences (in a different color, so it's clear they're reconstructed) so he can easily find the search terms he's looking for.

### Scenario 4:
Found a quote he likes in a document, but because the text is not embedded, he has to type it out by hand instead of being able to copy and paste. But because he's processed it through the app, he *can* easily copy and paste it.

### The Core
The ability to search a historical document with the text re-embedded or re-layered into the PDF. (Scenario 2 & 4)

## Supplemental
* Reconstructing text that is missing in the original
* Using a much more accurate OCR than existing OCR's (for these specific types of documents)
* Ability to view the document online and toggle new text on/off

## Storyboard & Wireframe

### Storyboard for Scenario 2
* Sitting on computer opening scanned files of books
* Opens file, skims through it
* Looking for a specific quote, but can't find it
* Tries searching, but the document isn't searchable
* Navigates to app webpage
* Logs in
* Drags and drops (or clicks upload button)
* Clicks the link to download the new document.

Found a long document that he needs to go through to see if there's anything useful in it, but because it's not searchable, he has to manually read through the entire thing. So he uploads it to the app, and it outputs a PDF he can easily search for keywords in.

### Wireframe in Moqup

[Click to view wireframe in Moqup](https://app.moqups.com/hePxLnsl2Jw0MpTlrXftiP8AS446wnJp/view/page/ac1a04925)

## User Epics
As a theology PhD student, I want to be able to easily upload and download (searchable versions of) PDF files so I can easily search old and difficult-to-read documents

## User Stories

### Story 1
As a theology PhD student, I want to see a front page with a video explaining how it works so I can evaluate if it's what I need, and see how to proceed

### Story 2
As a theology PhD student, I want to easily drag and drop to upload so I can quickly get the document back

### Story 3
As a theology PhD student, I want a simple link to download my document, so I can start searching it right away

### Story 4
As a theology PhD student, I want the outputted PDF to be searchable, so I can search it

### Story 5
As a theology PhD student, I want the searchable PDF to retain the same scanned images/text, so I can still use it as a historical document

### Story 6
As a theology PhD student, I want to see a progress bar or some other form of indicator that my request is being processed, so I don't have to worry if the conversion takes a long time.

## Technical Challenges (stuff I don't know how to do)
* Extracting the text into a PDF page of some kind
* layering a PDF with multiple layers (searchable)
* Uploading/downloading documents to cloud somehow (not saving) that can be accessed by a algorithm
* Building a simple cloud-hosted website

## Development Backlog

[Click to view backlog in Trello](https://trello.com/b/msgvvFoS)