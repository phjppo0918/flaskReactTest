import React from 'react';
import axios from "axios";

class JsonGet extends React.Component {
    constructor(props) {
        super(props);
        this.getStudy = this.getStudy.bind(this);
    }
    getStudy = () => {
        axios.get("/json").then(res => {
            console.log(res.data);
        });
    }
    componentDidMount() {
        this.getStudy();
    }

    render() {
        return <h1>send to Console</h1>
    }
    

}

export default JsonGet;