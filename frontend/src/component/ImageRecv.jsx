import React from 'react';
import axios from "axios";

class ImageRecv extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            image : null
        };
        this.getImage = this.getImage.bind(this);
   
    };

    getImage = () => {
      axios.get("/image", {responseType: "arraybuffer"})
      .then((res) => {
        const base64 = btoa(
            new Uint8Array(res.data).reduce(
                (data, byte) => data + String.fromCharCode(byte), ''
            )
        )
        console.log(base64);
        this.setState({image : base64})
      
    }
      )
    };

    componentDidMount() {
        this.getImage();
    }



    render() {
        return (
        <div>getImage <br/>
                <img src={`data:;base64,${this.state.image}`} alt="img" />
        </div>
        );
    }
}

export default ImageRecv;