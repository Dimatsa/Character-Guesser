import React, { Component } from 'react'
import './App.css';

class App extends React.Component {
  render() {
    return (
      <div>
        <title>Akinator</title>
        <h3>Akinator</h3>
        <form action="http://localhost:5000/guess/" method="GET" id="answer">
          <p>Check the answer to each true/false question, and click on the "Send Form" button to submit the information.</p>
          <p>1. Does your character have yellow skin:<br />
            <input type="radio" name="1. Does your character have yellow skin" defaultValue={1} />Yes<br />
            <input type="radio" name="1. Does your character have yellow skin" defaultValue={0} />No<br />
          </p>
          <p>2. Does your character live in the future:<br />
            <input type="radio" name="2. Does your character live in the future" defaultValue={1} />Yes<br />
            <input type="radio" name="2. Does your character live in the future" defaultValue={0} />No<br />
          </p>
          <p>3. Is your character an ape:<br />
            <input type="radio" name="3. Is your character an ape" defaultValue={1} />Yes<br />
            <input type="radio" name="3. Is your character an ape" defaultValue={0} />No<br />
          </p>
          <br />
          <br />
          <br />
          <br />
          <input type="submit" defaultValue="Send Form" />
          <input type="reset" defaultValue="Clear Form" />
        </form>
        <script src = "client.js"></script>
      </div>
    );
  }
}

export default App;
