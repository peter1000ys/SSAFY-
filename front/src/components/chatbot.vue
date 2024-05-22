<template>
  <div id="chat-container">
    <div id="chat-messages">
      <div v-for="(msg, index) in messages" :key="index" class="message">
        {{ msg.sender }}: {{ msg.message }}
      </div>
    </div>
    <div id="user-input">
      <input type="text" v-model="userInput" @keydown.enter="sendMessage" placeholder="메시지를 입력하세요..." />
      <button @click="sendMessage">전송</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const apiKey = '***REMOVED***';
const apiEndpoint = 'https://api.openai.com/v1/chat/completions';

const messages = ref([]);
const userInput = ref('');

function addMessage(sender, message) {
  messages.value.unshift({ sender, message });
}

async function fetchAIResponse(prompt) {
  const requestOptions = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${apiKey}`
    },
    body: JSON.stringify({
      model: "gpt-3.5-turbo",
      messages: [{ role: "user", content: prompt }],
      temperature: 0.8,
      max_tokens: 1024,
      top_p: 1,
      frequency_penalty: 0.5,
      presence_penalty: 0.5,
      stop: ["Human"],
    }),
  };
  try {
    const response = await fetch(apiEndpoint, requestOptions);
    const data = await response.json();
    const aiResponse = data.choices[0].message.content;
    return aiResponse;
  } catch (error) {
    console.error('OpenAI API 호출 중 오류 발생:', error);
    return 'OpenAI API 호출 중 오류 발생';
  }
}

async function sendMessage() {
  const message = userInput.value.trim();
  if (message.length === 0) return;
  addMessage('나', message);
  userInput.value = '';
  const aiResponse = await fetchAIResponse(message);
  addMessage('챗봇', aiResponse);
}
</script>

<style lang="scss" scoped>
body {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
}
.message {
  border-top: 1px solid #ccc;
  padding: 10px;
  margin-top: 5px;
  background-color: #e6e6e6;
}
#chat-container {
  width: 400px;
  height: 600px;
  display: flex;
  flex-direction: column;
  border: 1px solid #ccc;
}
#chat-messages {
  flex: 1;
  overflow-y: auto;
  padding: 10px;
  display: flex;
  flex-direction: column-reverse;
}
#user-input {
  display: flex;
  padding: 10px;
}
#user-input input {
  flex: 1;
  padding: 10px;
  outline: none;
}
#user-input button {
  border: none;
  background-color: #1e88e5;
  color: white;
  padding: 10px 15px;
  cursor: pointer;
}
</style>
