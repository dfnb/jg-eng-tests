import test from "node:test"
import assert from "node:assert/strict"
const { executeScenario } = await import(process.env.CHALLENGE_TARGET + "/src/app/public-api.ts")
function check(id,input,expected){test(id,()=>{try{assert.equal(executeScenario(input),expected);console.log(id+"|pass")}catch(error){console.log(id+"|fail|"+error.message);throw error}})}
check("C01","orders:read|home=,orders=orders:read","home,orders")
check("C02","|home=,admin=admin:read","home")
check("C03","a,b|one=a,two=b","one,two")
check("C04","x|public=,private=y","public")
check("C05","x|","")
