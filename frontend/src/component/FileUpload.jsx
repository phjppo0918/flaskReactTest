import React from 'react';
import axios from "axios";

class FileUpload extends React.Component {
    constructor(props) {
        super(props);
    
        this.state = {
          imageURL: '',
        };
    
        this.handleUploadImage = this.handleUploadImage.bind(this);
      }
    
      handleUploadImage(ev) {
        ev.preventDefault();
    
        const data = new FormData();
        data.append('file', this.uploadInput.files[0]);
        data.append('filename', this.fileName.value);
        axios({
            method: "post",
            url:"/image",
            data: data
        }).then((res) => {});
      }
    
      render() {
        return (
          <form onSubmit={this.handleUploadImage}>
            <div>
              <input ref={(ref) => { this.uploadInput = ref; }} type="file" />
            </div>
            <div>
              <input ref={(ref) => { this.fileName = ref; }} type="text" placeholder="Enter the desired name of file" />
            </div>
            <br />
            <div>
              <button>Upload</button>
            </div>
            <img src={this.state.imageURL} alt="img" />
          </form>
        );
      }
}

export default FileUpload;