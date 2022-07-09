import React from 'react';
import axios from "axios";

class JsonGet extends React.Component {
    constructor(props) {
        super(props);
        this.getJson = this.getJson.bind(this);
    }
    getJson = () => {
        axios.get("/json").then(res => {
            console.log(res.data);
        });
    }
    componentDidMount() {
        this.getJson();
    }

    render() {
        return <h1>get to Console</h1>
    }


}

export default JsonGet;