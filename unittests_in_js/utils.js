// Utility Module

const Utils = {
  calculateNumber(type, a, b) {
    let result = 0;
  
    if (type === 'SUM') {
      result = Math.round(a) + Math.round(b);
    } else if (type === 'SUBTRACT') {
      result = Math.round(a) - Math.round(b);
    } else if (type === 'DIVIDE') {
      if (Math.round(b) === 0) {
        return 'Error'
      } else {
        result = Math.round(a) / Math.round(b);
      }
      
    }
  
    return result;
  }
}

module.exports = Utils;
