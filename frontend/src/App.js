import './App.css';
import FileUpload from './component/FileUpload';
import JsonGet from './component/JsonGet';
import axios from 'axios';
import JsonSend from './component/JsonSend';
import ImageRecv from './component/ImageRecv';
axios.defaults.baseURL = 'http://127.0.0.1:5000'

function App() {
  return (
    <div className="App">
      <h1>file Upload</h1>
      <FileUpload />
      <JsonGet/>
      <JsonSend/>
      <ImageRecv/>
    </div>
  );
}

export default App;
