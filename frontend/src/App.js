import './App.css';
import FileUpload from './component/FileUpload';
import JsonGet from './component/JsonGet';
import axios from 'axios';

axios.defaults.baseURL = 'http://127.0.0.1:5000'

function App() {
  return (
    <div className="App">
      <h1>file Upload</h1>
      <FileUpload />
      <JsonGet/>
    </div>
  );
}

export default App;
