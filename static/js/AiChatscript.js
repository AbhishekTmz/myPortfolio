document.addEventListener("DOMContentLoaded", function () {
  const chatbox = document.getElementById("chatbot-box");
  const chatToggle = document.getElementById("chatbot-toggle");
  const chatClose = document.querySelector(".close-btn");
  const chatInput = document.getElementById("chatbot-input");
  const chatMessages = document.getElementById("chatbot-messages");
  
  // Track if this is first open
  let isFirstOpen = true;
  // Store chat history
  let chatHistory = [];
  
  // Create clear chat button in header
  const clearButton = document.createElement("button");
  clearButton.className = "clear-btn";
  clearButton.innerHTML = '<i class="fas fa-trash"></i>';
  clearButton.title = "Clear chat history";
  document.querySelector(".chatbot-header").appendChild(clearButton);

  // Add suggested questions buttons
  function addSuggestedQuestions() {
    const suggestions = [
      "What are your skills?",
      "Tell me about your projects",
      "What's your experience?",
      "How can I contact you?"
    ];
    
    const suggestionsContainer = document.createElement("div");
    suggestionsContainer.className = "suggested-questions";
    
    suggestions.forEach(question => {
      const button = document.createElement("button");
      button.className = "suggestion-btn";
      button.textContent = question;
      button.addEventListener("click", () => {
        chatInput.value = question;
        sendMessage();
      });
      suggestionsContainer.appendChild(button);
    });
    
    chatMessages.appendChild(suggestionsContainer);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  // Open chatbot
  chatToggle.addEventListener("click", () => {
    chatbox.classList.remove("hidden");
    
    // Show welcome message on first open
    if (isFirstOpen) {
      setTimeout(() => {
        appendMessage("AI Abhishek", "👋 Hi there! I'm Abhishek's AI assistant. How can I help you today?");
        addSuggestedQuestions();
        isFirstOpen = false;
      }, 500);
    }
  });

  // Close chatbot - Fixed to ensure it works
  chatClose.addEventListener("click", function() {
    chatbox.classList.add("hidden");
  });
  
  // Clear chat history
  clearButton.addEventListener("click", function() {
    chatMessages.innerHTML = "";
    chatHistory = [];
    setTimeout(() => {
      appendMessage("AI Abhishek", "Chat history cleared. How can I help you?");
    }, 300);
  });

  // Send message function
  function sendMessage() {
    const message = chatInput.value.trim();
    if (!message) return;
    
    // Add to chat history
    chatHistory.push({ sender: "You", message: message });
    
    // Display user message
    appendMessage("You", message);
    chatInput.value = "";
    
    // Show typing indicator
    const typingIndicator = document.createElement("div");
    typingIndicator.className = "chatbot-message ai typing-indicator";
    typingIndicator.innerHTML = "<span>AI Abhishek is typing</span><span class='dot-1'>.</span><span class='dot-2'>.</span><span class='dot-3'>.</span>";
    chatMessages.appendChild(typingIndicator);
    chatMessages.scrollTop = chatMessages.scrollHeight;

    // Send to backend
    fetch("/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message }),
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error("Network response was not ok");
        }
        return res.json();
      })
      .then((data) => {
        // Remove typing indicator
        chatMessages.removeChild(typingIndicator);
        
        // Add to chat history
        chatHistory.push({ sender: "AI Abhishek", message: data.response });
        
        // Display AI response
        appendMessage("AI Abhishek", data.response || "Sorry, I didn't get that.");
      })
      .catch((error) => {
        console.error("Error:", error);
        // Remove typing indicator
        chatMessages.removeChild(typingIndicator);
        appendMessage("AI Abhishek", "There was an error. Please try again later.");
      });
  }

  // Handle Enter key
  chatInput.addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
      sendMessage();
    }
  });

  // Append message with bubble styling and timestamp
  function appendMessage(sender, text) {
    const msg = document.createElement("div");
    msg.className = "chatbot-message " + (sender === "You" ? "user" : "ai");
    
    // Get current time
    const now = new Date();
    const timeString = now.getHours().toString().padStart(2, '0') + ':' + 
                      now.getMinutes().toString().padStart(2, '0');
    
    // Format message with sender, text and time
    msg.innerHTML = `
      <div class="message-header">
        <strong>${sender}</strong>
        <span class="message-time">${timeString}</span>
      </div>
      <div class="message-content">${text}</div>
    `;
    
    chatMessages.appendChild(msg);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }
  
  // Focus input when chat is opened
  chatToggle.addEventListener("click", () => {
    setTimeout(() => chatInput.focus(), 100);
  });

  // Save chat history to localStorage
  function saveHistory() {
    localStorage.setItem('chatHistory', JSON.stringify(chatHistory));
  }

  // Load chat history from localStorage
  function loadHistory() {
    const saved = localStorage.getItem('chatHistory');
    if (saved) {
      chatHistory = JSON.parse(saved);
      chatHistory.forEach(item => {
        appendMessage(item.sender, item.message);
      });
      isFirstOpen = false;
    }
  }

  // Try to load history when page loads
  loadHistory();
});
