import React from 'react';
import axios from "axios";

class JsonSend extends React.Component {
    constructor(props) {
        super(props);
        this.postJson = this.postJson.bind(this);
    }
    postJson = () => {
        axios.post("/json",{aa:"1234", bb:234})
    }
    componentDidMount() {
        this.postJson();
    }

    render() {
        return <h1>send to server</h1>
    }
    

}

export default JsonSend;