# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aptos/transaction/v1/transaction.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from aptos.util.timestamp import (
    timestamp_pb2 as aptos_dot_util_dot_timestamp_dot_timestamp__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n&aptos/transaction/v1/transaction.proto\x12\x14\x61ptos.transaction.v1\x1a$aptos/util/timestamp/timestamp.proto"\x9a\x01\n\x05\x42lock\x12\x32\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1f.aptos.util.timestamp.Timestamp\x12\x12\n\x06height\x18\x02 \x01(\x04\x42\x02\x30\x01\x12\x37\n\x0ctransactions\x18\x03 \x03(\x0b\x32!.aptos.transaction.v1.Transaction\x12\x10\n\x08\x63hain_id\x18\x04 \x01(\r"\xcc\x05\n\x0bTransaction\x12\x32\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1f.aptos.util.timestamp.Timestamp\x12\x13\n\x07version\x18\x02 \x01(\x04\x42\x02\x30\x01\x12\x33\n\x04info\x18\x03 \x01(\x0b\x32%.aptos.transaction.v1.TransactionInfo\x12\x11\n\x05\x65poch\x18\x04 \x01(\x04\x42\x02\x30\x01\x12\x18\n\x0c\x62lock_height\x18\x05 \x01(\x04\x42\x02\x30\x01\x12?\n\x04type\x18\x06 \x01(\x0e\x32\x31.aptos.transaction.v1.Transaction.TransactionType\x12H\n\x0e\x62lock_metadata\x18\x07 \x01(\x0b\x32..aptos.transaction.v1.BlockMetadataTransactionH\x00\x12;\n\x07genesis\x18\x08 \x01(\x0b\x32(.aptos.transaction.v1.GenesisTransactionH\x00\x12L\n\x10state_checkpoint\x18\t \x01(\x0b\x32\x30.aptos.transaction.v1.StateCheckpointTransactionH\x00\x12\x35\n\x04user\x18\n \x01(\x0b\x32%.aptos.transaction.v1.UserTransactionH\x00"\xb8\x01\n\x0fTransactionType\x12 \n\x1cTRANSACTION_TYPE_UNSPECIFIED\x10\x00\x12\x1c\n\x18TRANSACTION_TYPE_GENESIS\x10\x01\x12#\n\x1fTRANSACTION_TYPE_BLOCK_METADATA\x10\x02\x12%\n!TRANSACTION_TYPE_STATE_CHECKPOINT\x10\x03\x12\x19\n\x15TRANSACTION_TYPE_USER\x10\x04\x42\n\n\x08txn_data"\xbe\x01\n\x18\x42lockMetadataTransaction\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\x05round\x18\x02 \x01(\x04\x42\x02\x30\x01\x12+\n\x06\x65vents\x18\x03 \x03(\x0b\x32\x1b.aptos.transaction.v1.Event\x12#\n\x1bprevious_block_votes_bitvec\x18\x04 \x01(\x0c\x12\x10\n\x08proposer\x18\x05 \x01(\t\x12\x1f\n\x17\x66\x61iled_proposer_indices\x18\x06 \x03(\r"r\n\x12GenesisTransaction\x12/\n\x07payload\x18\x01 \x01(\x0b\x32\x1e.aptos.transaction.v1.WriteSet\x12+\n\x06\x65vents\x18\x02 \x03(\x0b\x32\x1b.aptos.transaction.v1.Event"\x1c\n\x1aStateCheckpointTransaction"}\n\x0fUserTransaction\x12=\n\x07request\x18\x01 \x01(\x0b\x32,.aptos.transaction.v1.UserTransactionRequest\x12+\n\x06\x65vents\x18\x02 \x03(\x0b\x32\x1b.aptos.transaction.v1.Event"\x9f\x01\n\x05\x45vent\x12+\n\x03key\x18\x01 \x01(\x0b\x32\x1e.aptos.transaction.v1.EventKey\x12\x1b\n\x0fsequence_number\x18\x02 \x01(\x04\x42\x02\x30\x01\x12,\n\x04type\x18\x03 \x01(\x0b\x32\x1e.aptos.transaction.v1.MoveType\x12\x10\n\x08type_str\x18\x05 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\t"\xa1\x02\n\x0fTransactionInfo\x12\x0c\n\x04hash\x18\x01 \x01(\x0c\x12\x19\n\x11state_change_hash\x18\x02 \x01(\x0c\x12\x17\n\x0f\x65vent_root_hash\x18\x03 \x01(\x0c\x12"\n\x15state_checkpoint_hash\x18\x04 \x01(\x0cH\x00\x88\x01\x01\x12\x14\n\x08gas_used\x18\x05 \x01(\x04\x42\x02\x30\x01\x12\x0f\n\x07success\x18\x06 \x01(\x08\x12\x11\n\tvm_status\x18\x07 \x01(\t\x12\x1d\n\x15\x61\x63\x63umulator_root_hash\x18\x08 \x01(\x0c\x12\x35\n\x07\x63hanges\x18\t \x03(\x0b\x32$.aptos.transaction.v1.WriteSetChangeB\x18\n\x16_state_checkpoint_hash"@\n\x08\x45ventKey\x12\x1b\n\x0f\x63reation_number\x18\x01 \x01(\x04\x42\x02\x30\x01\x12\x17\n\x0f\x61\x63\x63ount_address\x18\x02 \x01(\t"\xb0\x02\n\x16UserTransactionRequest\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x1b\n\x0fsequence_number\x18\x02 \x01(\x04\x42\x02\x30\x01\x12\x1a\n\x0emax_gas_amount\x18\x03 \x01(\x04\x42\x02\x30\x01\x12\x1a\n\x0egas_unit_price\x18\x04 \x01(\x04\x42\x02\x30\x01\x12\x42\n\x19\x65xpiration_timestamp_secs\x18\x05 \x01(\x0b\x32\x1f.aptos.util.timestamp.Timestamp\x12\x39\n\x07payload\x18\x06 \x01(\x0b\x32(.aptos.transaction.v1.TransactionPayload\x12\x32\n\tsignature\x18\x07 \x01(\x0b\x32\x1f.aptos.transaction.v1.Signature"\xda\x02\n\x08WriteSet\x12\x43\n\x0ewrite_set_type\x18\x01 \x01(\x0e\x32+.aptos.transaction.v1.WriteSet.WriteSetType\x12@\n\x10script_write_set\x18\x02 \x01(\x0b\x32$.aptos.transaction.v1.ScriptWriteSetH\x00\x12@\n\x10\x64irect_write_set\x18\x03 \x01(\x0b\x32$.aptos.transaction.v1.DirectWriteSetH\x00"x\n\x0cWriteSetType\x12\x1e\n\x1aWRITE_SET_TYPE_UNSPECIFIED\x10\x00\x12#\n\x1fWRITE_SET_TYPE_SCRIPT_WRITE_SET\x10\x01\x12#\n\x1fWRITE_SET_TYPE_DIRECT_WRITE_SET\x10\x02\x42\x0b\n\twrite_set"Y\n\x0eScriptWriteSet\x12\x12\n\nexecute_as\x18\x01 \x01(\t\x12\x33\n\x06script\x18\x02 \x01(\x0b\x32#.aptos.transaction.v1.ScriptPayload"}\n\x0e\x44irectWriteSet\x12>\n\x10write_set_change\x18\x01 \x03(\x0b\x32$.aptos.transaction.v1.WriteSetChange\x12+\n\x06\x65vents\x18\x02 \x03(\x0b\x32\x1b.aptos.transaction.v1.Event"\x89\x05\n\x0eWriteSetChange\x12\x37\n\x04type\x18\x01 \x01(\x0e\x32).aptos.transaction.v1.WriteSetChange.Type\x12;\n\rdelete_module\x18\x02 \x01(\x0b\x32".aptos.transaction.v1.DeleteModuleH\x00\x12?\n\x0f\x64\x65lete_resource\x18\x03 \x01(\x0b\x32$.aptos.transaction.v1.DeleteResourceH\x00\x12\x42\n\x11\x64\x65lete_table_item\x18\x04 \x01(\x0b\x32%.aptos.transaction.v1.DeleteTableItemH\x00\x12\x39\n\x0cwrite_module\x18\x05 \x01(\x0b\x32!.aptos.transaction.v1.WriteModuleH\x00\x12=\n\x0ewrite_resource\x18\x06 \x01(\x0b\x32#.aptos.transaction.v1.WriteResourceH\x00\x12@\n\x10write_table_item\x18\x07 \x01(\x0b\x32$.aptos.transaction.v1.WriteTableItemH\x00"\xb5\x01\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12TYPE_DELETE_MODULE\x10\x01\x12\x18\n\x14TYPE_DELETE_RESOURCE\x10\x02\x12\x1a\n\x16TYPE_DELETE_TABLE_ITEM\x10\x03\x12\x15\n\x11TYPE_WRITE_MODULE\x10\x04\x12\x17\n\x13TYPE_WRITE_RESOURCE\x10\x05\x12\x19\n\x15TYPE_WRITE_TABLE_ITEM\x10\x06\x42\x08\n\x06\x63hange"k\n\x0c\x44\x65leteModule\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x16\n\x0estate_key_hash\x18\x02 \x01(\x0c\x12\x32\n\x06module\x18\x03 \x01(\x0b\x32".aptos.transaction.v1.MoveModuleId"~\n\x0e\x44\x65leteResource\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x16\n\x0estate_key_hash\x18\x02 \x01(\x0c\x12\x31\n\x04type\x18\x03 \x01(\x0b\x32#.aptos.transaction.v1.MoveStructTag\x12\x10\n\x08type_str\x18\x04 \x01(\t"{\n\x0f\x44\x65leteTableItem\x12\x16\n\x0estate_key_hash\x18\x01 \x01(\x0c\x12\x0e\n\x06handle\x18\x02 \x01(\t\x12\x0b\n\x03key\x18\x03 \x01(\t\x12\x33\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32%.aptos.transaction.v1.DeleteTableData"0\n\x0f\x44\x65leteTableData\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x10\n\x08key_type\x18\x02 \x01(\t"n\n\x0bWriteModule\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x16\n\x0estate_key_hash\x18\x02 \x01(\x0c\x12\x36\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32(.aptos.transaction.v1.MoveModuleBytecode"\x8b\x01\n\rWriteResource\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x16\n\x0estate_key_hash\x18\x02 \x01(\x0c\x12\x31\n\x04type\x18\x03 \x01(\x0b\x32#.aptos.transaction.v1.MoveStructTag\x12\x10\n\x08type_str\x18\x04 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x05 \x01(\t"R\n\x0eWriteTableData\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x10\n\x08key_type\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\x12\x12\n\nvalue_type\x18\x04 \x01(\t"y\n\x0eWriteTableItem\x12\x16\n\x0estate_key_hash\x18\x01 \x01(\x0c\x12\x0e\n\x06handle\x18\x02 \x01(\t\x12\x0b\n\x03key\x18\x03 \x01(\t\x12\x32\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32$.aptos.transaction.v1.WriteTableData"\xec\x04\n\x12TransactionPayload\x12;\n\x04type\x18\x01 \x01(\x0e\x32-.aptos.transaction.v1.TransactionPayload.Type\x12L\n\x16\x65ntry_function_payload\x18\x02 \x01(\x0b\x32*.aptos.transaction.v1.EntryFunctionPayloadH\x00\x12=\n\x0escript_payload\x18\x03 \x01(\x0b\x32#.aptos.transaction.v1.ScriptPayloadH\x00\x12J\n\x15module_bundle_payload\x18\x04 \x01(\x0b\x32).aptos.transaction.v1.ModuleBundlePayloadH\x00\x12\x42\n\x11write_set_payload\x18\x05 \x01(\x0b\x32%.aptos.transaction.v1.WriteSetPayloadH\x00\x12\x41\n\x10multisig_payload\x18\x06 \x01(\x0b\x32%.aptos.transaction.v1.MultisigPayloadH\x00"\xad\x01\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x1f\n\x1bTYPE_ENTRY_FUNCTION_PAYLOAD\x10\x01\x12\x17\n\x13TYPE_SCRIPT_PAYLOAD\x10\x02\x12\x1e\n\x1aTYPE_MODULE_BUNDLE_PAYLOAD\x10\x03\x12\x1a\n\x16TYPE_WRITE_SET_PAYLOAD\x10\x04\x12\x19\n\x15TYPE_MULTISIG_PAYLOAD\x10\x05\x42\t\n\x07payload"\xb9\x01\n\x14\x45ntryFunctionPayload\x12\x37\n\x08\x66unction\x18\x01 \x01(\x0b\x32%.aptos.transaction.v1.EntryFunctionId\x12\x36\n\x0etype_arguments\x18\x02 \x03(\x0b\x32\x1e.aptos.transaction.v1.MoveType\x12\x11\n\targuments\x18\x03 \x03(\t\x12\x1d\n\x15\x65ntry_function_id_str\x18\x04 \x01(\t"W\n\x12MoveScriptBytecode\x12\x10\n\x08\x62ytecode\x18\x01 \x01(\x0c\x12/\n\x03\x61\x62i\x18\x02 \x01(\x0b\x32".aptos.transaction.v1.MoveFunction"\x92\x01\n\rScriptPayload\x12\x36\n\x04\x63ode\x18\x01 \x01(\x0b\x32(.aptos.transaction.v1.MoveScriptBytecode\x12\x36\n\x0etype_arguments\x18\x02 \x03(\x0b\x32\x1e.aptos.transaction.v1.MoveType\x12\x11\n\targuments\x18\x03 \x03(\t"\x97\x01\n\x0fMultisigPayload\x12\x18\n\x10multisig_address\x18\x01 \x01(\t\x12R\n\x13transaction_payload\x18\x02 \x01(\x0b\x32\x30.aptos.transaction.v1.MultisigTransactionPayloadH\x00\x88\x01\x01\x42\x16\n\x14_transaction_payload"\xf9\x01\n\x1aMultisigTransactionPayload\x12\x43\n\x04type\x18\x01 \x01(\x0e\x32\x35.aptos.transaction.v1.MultisigTransactionPayload.Type\x12L\n\x16\x65ntry_function_payload\x18\x02 \x01(\x0b\x32*.aptos.transaction.v1.EntryFunctionPayloadH\x00"=\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x1f\n\x1bTYPE_ENTRY_FUNCTION_PAYLOAD\x10\x01\x42\t\n\x07payload"P\n\x13ModuleBundlePayload\x12\x39\n\x07modules\x18\x01 \x03(\x0b\x32(.aptos.transaction.v1.MoveModuleBytecode"U\n\x12MoveModuleBytecode\x12\x10\n\x08\x62ytecode\x18\x01 \x01(\x0c\x12-\n\x03\x61\x62i\x18\x02 \x01(\x0b\x32 .aptos.transaction.v1.MoveModule"\xd2\x01\n\nMoveModule\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x33\n\x07\x66riends\x18\x03 \x03(\x0b\x32".aptos.transaction.v1.MoveModuleId\x12=\n\x11\x65xposed_functions\x18\x04 \x03(\x0b\x32".aptos.transaction.v1.MoveFunction\x12\x31\n\x07structs\x18\x05 \x03(\x0b\x32 .aptos.transaction.v1.MoveStruct"\x92\x03\n\x0cMoveFunction\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x41\n\nvisibility\x18\x02 \x01(\x0e\x32-.aptos.transaction.v1.MoveFunction.Visibility\x12\x10\n\x08is_entry\x18\x03 \x01(\x08\x12O\n\x13generic_type_params\x18\x04 \x03(\x0b\x32\x32.aptos.transaction.v1.MoveFunctionGenericTypeParam\x12.\n\x06params\x18\x05 \x03(\x0b\x32\x1e.aptos.transaction.v1.MoveType\x12.\n\x06return\x18\x06 \x03(\x0b\x32\x1e.aptos.transaction.v1.MoveType"n\n\nVisibility\x12\x1a\n\x16VISIBILITY_UNSPECIFIED\x10\x00\x12\x16\n\x12VISIBILITY_PRIVATE\x10\x01\x12\x15\n\x11VISIBILITY_PUBLIC\x10\x02\x12\x15\n\x11VISIBILITY_FRIEND\x10\x03"\xe9\x01\n\nMoveStruct\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tis_native\x18\x02 \x01(\x08\x12\x34\n\tabilities\x18\x03 \x03(\x0e\x32!.aptos.transaction.v1.MoveAbility\x12M\n\x13generic_type_params\x18\x04 \x03(\x0b\x32\x30.aptos.transaction.v1.MoveStructGenericTypeParam\x12\x35\n\x06\x66ields\x18\x05 \x03(\x0b\x32%.aptos.transaction.v1.MoveStructField"h\n\x1aMoveStructGenericTypeParam\x12\x36\n\x0b\x63onstraints\x18\x01 \x03(\x0e\x32!.aptos.transaction.v1.MoveAbility\x12\x12\n\nis_phantom\x18\x02 \x01(\x08"M\n\x0fMoveStructField\x12\x0c\n\x04name\x18\x01 \x01(\t\x12,\n\x04type\x18\x02 \x01(\x0b\x32\x1e.aptos.transaction.v1.MoveType"V\n\x1cMoveFunctionGenericTypeParam\x12\x36\n\x0b\x63onstraints\x18\x01 \x03(\x0e\x32!.aptos.transaction.v1.MoveAbility"\xf8\x02\n\x08MoveType\x12-\n\x04type\x18\x01 \x01(\x0e\x32\x1f.aptos.transaction.v1.MoveTypes\x12\x30\n\x06vector\x18\x03 \x01(\x0b\x32\x1e.aptos.transaction.v1.MoveTypeH\x00\x12\x35\n\x06struct\x18\x04 \x01(\x0b\x32#.aptos.transaction.v1.MoveStructTagH\x00\x12"\n\x18generic_type_param_index\x18\x05 \x01(\rH\x00\x12\x41\n\treference\x18\x06 \x01(\x0b\x32,.aptos.transaction.v1.MoveType.ReferenceTypeH\x00\x12\x14\n\nunparsable\x18\x07 \x01(\tH\x00\x1aL\n\rReferenceType\x12\x0f\n\x07mutable\x18\x01 \x01(\x08\x12*\n\x02to\x18\x02 \x01(\x0b\x32\x1e.aptos.transaction.v1.MoveTypeB\t\n\x07\x63ontent"D\n\x0fWriteSetPayload\x12\x31\n\twrite_set\x18\x01 \x01(\x0b\x32\x1e.aptos.transaction.v1.WriteSet"S\n\x0f\x45ntryFunctionId\x12\x32\n\x06module\x18\x01 \x01(\x0b\x32".aptos.transaction.v1.MoveModuleId\x12\x0c\n\x04name\x18\x02 \x01(\t"-\n\x0cMoveModuleId\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t"{\n\rMoveStructTag\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0e\n\x06module\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12;\n\x13generic_type_params\x18\x04 \x03(\x0b\x32\x1e.aptos.transaction.v1.MoveType"\xa4\x04\n\tSignature\x12\x32\n\x04type\x18\x01 \x01(\x0e\x32$.aptos.transaction.v1.Signature.Type\x12\x39\n\x07\x65\x64\x32\x35\x35\x31\x39\x18\x02 \x01(\x0b\x32&.aptos.transaction.v1.Ed25519SignatureH\x00\x12\x44\n\rmulti_ed25519\x18\x03 \x01(\x0b\x32+.aptos.transaction.v1.MultiEd25519SignatureH\x00\x12@\n\x0bmulti_agent\x18\x04 \x01(\x0b\x32).aptos.transaction.v1.MultiAgentSignatureH\x00\x12<\n\tfee_payer\x18\x05 \x01(\x0b\x32\'.aptos.transaction.v1.FeePayerSignatureH\x00\x12H\n\x0fsecp256k1_ecdsa\x18\x06 \x01(\x0b\x32-.aptos.transaction.v1.Secp256k1ECDSASignatureH\x00"\x8a\x01\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x10\n\x0cTYPE_ED25519\x10\x01\x12\x16\n\x12TYPE_MULTI_ED25519\x10\x02\x12\x14\n\x10TYPE_MULTI_AGENT\x10\x03\x12\x12\n\x0eTYPE_FEE_PAYER\x10\x04\x12\x18\n\x14TYPE_SECP256K1_ECDSA\x10\x05\x42\x0b\n\tsignature"9\n\x10\x45\x64\x32\x35\x35\x31\x39Signature\x12\x12\n\npublic_key\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c"o\n\x15MultiEd25519Signature\x12\x13\n\x0bpublic_keys\x18\x01 \x03(\x0c\x12\x12\n\nsignatures\x18\x02 \x03(\x0c\x12\x11\n\tthreshold\x18\x03 \x01(\r\x12\x1a\n\x12public_key_indices\x18\x04 \x03(\r"\xb4\x01\n\x13MultiAgentSignature\x12\x36\n\x06sender\x18\x01 \x01(\x0b\x32&.aptos.transaction.v1.AccountSignature\x12"\n\x1asecondary_signer_addresses\x18\x02 \x03(\t\x12\x41\n\x11secondary_signers\x18\x03 \x03(\x0b\x32&.aptos.transaction.v1.AccountSignature"\x8f\x02\n\x11\x46\x65\x65PayerSignature\x12\x36\n\x06sender\x18\x01 \x01(\x0b\x32&.aptos.transaction.v1.AccountSignature\x12"\n\x1asecondary_signer_addresses\x18\x02 \x03(\t\x12\x41\n\x11secondary_signers\x18\x03 \x03(\x0b\x32&.aptos.transaction.v1.AccountSignature\x12\x19\n\x11\x66\x65\x65_payer_address\x18\x04 \x01(\t\x12@\n\x10\x66\x65\x65_payer_signer\x18\x05 \x01(\x0b\x32&.aptos.transaction.v1.AccountSignature"@\n\x17Secp256k1ECDSASignature\x12\x12\n\npublic_key\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c"\x87\x03\n\x10\x41\x63\x63ountSignature\x12\x39\n\x04type\x18\x01 \x01(\x0e\x32+.aptos.transaction.v1.AccountSignature.Type\x12\x39\n\x07\x65\x64\x32\x35\x35\x31\x39\x18\x02 \x01(\x0b\x32&.aptos.transaction.v1.Ed25519SignatureH\x00\x12\x44\n\rmulti_ed25519\x18\x03 \x01(\x0b\x32+.aptos.transaction.v1.MultiEd25519SignatureH\x00\x12H\n\x0fsecp256k1_ecdsa\x18\x04 \x01(\x0b\x32-.aptos.transaction.v1.Secp256k1ECDSASignatureH\x00"`\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x10\n\x0cTYPE_ED25519\x10\x01\x12\x16\n\x12TYPE_MULTI_ED25519\x10\x02\x12\x18\n\x14TYPE_SECP256K1_ECDSA\x10\x03\x42\x0b\n\tsignature*\xea\x02\n\tMoveTypes\x12\x1a\n\x16MOVE_TYPES_UNSPECIFIED\x10\x00\x12\x13\n\x0fMOVE_TYPES_BOOL\x10\x01\x12\x11\n\rMOVE_TYPES_U8\x10\x02\x12\x12\n\x0eMOVE_TYPES_U16\x10\x0c\x12\x12\n\x0eMOVE_TYPES_U32\x10\r\x12\x12\n\x0eMOVE_TYPES_U64\x10\x03\x12\x13\n\x0fMOVE_TYPES_U128\x10\x04\x12\x13\n\x0fMOVE_TYPES_U256\x10\x0e\x12\x16\n\x12MOVE_TYPES_ADDRESS\x10\x05\x12\x15\n\x11MOVE_TYPES_SIGNER\x10\x06\x12\x15\n\x11MOVE_TYPES_VECTOR\x10\x07\x12\x15\n\x11MOVE_TYPES_STRUCT\x10\x08\x12!\n\x1dMOVE_TYPES_GENERIC_TYPE_PARAM\x10\t\x12\x18\n\x14MOVE_TYPES_REFERENCE\x10\n\x12\x19\n\x15MOVE_TYPES_UNPARSABLE\x10\x0b*\x87\x01\n\x0bMoveAbility\x12\x1c\n\x18MOVE_ABILITY_UNSPECIFIED\x10\x00\x12\x15\n\x11MOVE_ABILITY_COPY\x10\x01\x12\x15\n\x11MOVE_ABILITY_DROP\x10\x02\x12\x16\n\x12MOVE_ABILITY_STORE\x10\x03\x12\x14\n\x10MOVE_ABILITY_KEY\x10\x04\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "aptos.transaction.v1.transaction_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _BLOCK.fields_by_name["height"]._options = None
    _BLOCK.fields_by_name["height"]._serialized_options = b"0\001"
    _TRANSACTION.fields_by_name["version"]._options = None
    _TRANSACTION.fields_by_name["version"]._serialized_options = b"0\001"
    _TRANSACTION.fields_by_name["epoch"]._options = None
    _TRANSACTION.fields_by_name["epoch"]._serialized_options = b"0\001"
    _TRANSACTION.fields_by_name["block_height"]._options = None
    _TRANSACTION.fields_by_name["block_height"]._serialized_options = b"0\001"
    _BLOCKMETADATATRANSACTION.fields_by_name["round"]._options = None
    _BLOCKMETADATATRANSACTION.fields_by_name["round"]._serialized_options = b"0\001"
    _EVENT.fields_by_name["sequence_number"]._options = None
    _EVENT.fields_by_name["sequence_number"]._serialized_options = b"0\001"
    _TRANSACTIONINFO.fields_by_name["gas_used"]._options = None
    _TRANSACTIONINFO.fields_by_name["gas_used"]._serialized_options = b"0\001"
    _EVENTKEY.fields_by_name["creation_number"]._options = None
    _EVENTKEY.fields_by_name["creation_number"]._serialized_options = b"0\001"
    _USERTRANSACTIONREQUEST.fields_by_name["sequence_number"]._options = None
    _USERTRANSACTIONREQUEST.fields_by_name[
        "sequence_number"
    ]._serialized_options = b"0\001"
    _USERTRANSACTIONREQUEST.fields_by_name["max_gas_amount"]._options = None
    _USERTRANSACTIONREQUEST.fields_by_name[
        "max_gas_amount"
    ]._serialized_options = b"0\001"
    _USERTRANSACTIONREQUEST.fields_by_name["gas_unit_price"]._options = None
    _USERTRANSACTIONREQUEST.fields_by_name[
        "gas_unit_price"
    ]._serialized_options = b"0\001"
    _globals["_MOVETYPES"]._serialized_start = 9461
    _globals["_MOVETYPES"]._serialized_end = 9823
    _globals["_MOVEABILITY"]._serialized_start = 9826
    _globals["_MOVEABILITY"]._serialized_end = 9961
    _globals["_BLOCK"]._serialized_start = 103
    _globals["_BLOCK"]._serialized_end = 257
    _globals["_TRANSACTION"]._serialized_start = 260
    _globals["_TRANSACTION"]._serialized_end = 976
    _globals["_TRANSACTION_TRANSACTIONTYPE"]._serialized_start = 780
    _globals["_TRANSACTION_TRANSACTIONTYPE"]._serialized_end = 964
    _globals["_BLOCKMETADATATRANSACTION"]._serialized_start = 979
    _globals["_BLOCKMETADATATRANSACTION"]._serialized_end = 1169
    _globals["_GENESISTRANSACTION"]._serialized_start = 1171
    _globals["_GENESISTRANSACTION"]._serialized_end = 1285
    _globals["_STATECHECKPOINTTRANSACTION"]._serialized_start = 1287
    _globals["_STATECHECKPOINTTRANSACTION"]._serialized_end = 1315
    _globals["_USERTRANSACTION"]._serialized_start = 1317
    _globals["_USERTRANSACTION"]._serialized_end = 1442
    _globals["_EVENT"]._serialized_start = 1445
    _globals["_EVENT"]._serialized_end = 1604
    _globals["_TRANSACTIONINFO"]._serialized_start = 1607
    _globals["_TRANSACTIONINFO"]._serialized_end = 1896
    _globals["_EVENTKEY"]._serialized_start = 1898
    _globals["_EVENTKEY"]._serialized_end = 1962
    _globals["_USERTRANSACTIONREQUEST"]._serialized_start = 1965
    _globals["_USERTRANSACTIONREQUEST"]._serialized_end = 2269
    _globals["_WRITESET"]._serialized_start = 2272
    _globals["_WRITESET"]._serialized_end = 2618
    _globals["_WRITESET_WRITESETTYPE"]._serialized_start = 2485
    _globals["_WRITESET_WRITESETTYPE"]._serialized_end = 2605
    _globals["_SCRIPTWRITESET"]._serialized_start = 2620
    _globals["_SCRIPTWRITESET"]._serialized_end = 2709
    _globals["_DIRECTWRITESET"]._serialized_start = 2711
    _globals["_DIRECTWRITESET"]._serialized_end = 2836
    _globals["_WRITESETCHANGE"]._serialized_start = 2839
    _globals["_WRITESETCHANGE"]._serialized_end = 3488
    _globals["_WRITESETCHANGE_TYPE"]._serialized_start = 3297
    _globals["_WRITESETCHANGE_TYPE"]._serialized_end = 3478
    _globals["_DELETEMODULE"]._serialized_start = 3490
    _globals["_DELETEMODULE"]._serialized_end = 3597
    _globals["_DELETERESOURCE"]._serialized_start = 3599
    _globals["_DELETERESOURCE"]._serialized_end = 3725
    _globals["_DELETETABLEITEM"]._serialized_start = 3727
    _globals["_DELETETABLEITEM"]._serialized_end = 3850
    _globals["_DELETETABLEDATA"]._serialized_start = 3852
    _globals["_DELETETABLEDATA"]._serialized_end = 3900
    _globals["_WRITEMODULE"]._serialized_start = 3902
    _globals["_WRITEMODULE"]._serialized_end = 4012
    _globals["_WRITERESOURCE"]._serialized_start = 4015
    _globals["_WRITERESOURCE"]._serialized_end = 4154
    _globals["_WRITETABLEDATA"]._serialized_start = 4156
    _globals["_WRITETABLEDATA"]._serialized_end = 4238
    _globals["_WRITETABLEITEM"]._serialized_start = 4240
    _globals["_WRITETABLEITEM"]._serialized_end = 4361
    _globals["_TRANSACTIONPAYLOAD"]._serialized_start = 4364
    _globals["_TRANSACTIONPAYLOAD"]._serialized_end = 4984
    _globals["_TRANSACTIONPAYLOAD_TYPE"]._serialized_start = 4800
    _globals["_TRANSACTIONPAYLOAD_TYPE"]._serialized_end = 4973
    _globals["_ENTRYFUNCTIONPAYLOAD"]._serialized_start = 4987
    _globals["_ENTRYFUNCTIONPAYLOAD"]._serialized_end = 5172
    _globals["_MOVESCRIPTBYTECODE"]._serialized_start = 5174
    _globals["_MOVESCRIPTBYTECODE"]._serialized_end = 5261
    _globals["_SCRIPTPAYLOAD"]._serialized_start = 5264
    _globals["_SCRIPTPAYLOAD"]._serialized_end = 5410
    _globals["_MULTISIGPAYLOAD"]._serialized_start = 5413
    _globals["_MULTISIGPAYLOAD"]._serialized_end = 5564
    _globals["_MULTISIGTRANSACTIONPAYLOAD"]._serialized_start = 5567
    _globals["_MULTISIGTRANSACTIONPAYLOAD"]._serialized_end = 5816
    _globals["_MULTISIGTRANSACTIONPAYLOAD_TYPE"]._serialized_start = 4800
    _globals["_MULTISIGTRANSACTIONPAYLOAD_TYPE"]._serialized_end = 4861
    _globals["_MODULEBUNDLEPAYLOAD"]._serialized_start = 5818
    _globals["_MODULEBUNDLEPAYLOAD"]._serialized_end = 5898
    _globals["_MOVEMODULEBYTECODE"]._serialized_start = 5900
    _globals["_MOVEMODULEBYTECODE"]._serialized_end = 5985
    _globals["_MOVEMODULE"]._serialized_start = 5988
    _globals["_MOVEMODULE"]._serialized_end = 6198
    _globals["_MOVEFUNCTION"]._serialized_start = 6201
    _globals["_MOVEFUNCTION"]._serialized_end = 6603
    _globals["_MOVEFUNCTION_VISIBILITY"]._serialized_start = 6493
    _globals["_MOVEFUNCTION_VISIBILITY"]._serialized_end = 6603
    _globals["_MOVESTRUCT"]._serialized_start = 6606
    _globals["_MOVESTRUCT"]._serialized_end = 6839
    _globals["_MOVESTRUCTGENERICTYPEPARAM"]._serialized_start = 6841
    _globals["_MOVESTRUCTGENERICTYPEPARAM"]._serialized_end = 6945
    _globals["_MOVESTRUCTFIELD"]._serialized_start = 6947
    _globals["_MOVESTRUCTFIELD"]._serialized_end = 7024
    _globals["_MOVEFUNCTIONGENERICTYPEPARAM"]._serialized_start = 7026
    _globals["_MOVEFUNCTIONGENERICTYPEPARAM"]._serialized_end = 7112
    _globals["_MOVETYPE"]._serialized_start = 7115
    _globals["_MOVETYPE"]._serialized_end = 7491
    _globals["_MOVETYPE_REFERENCETYPE"]._serialized_start = 7404
    _globals["_MOVETYPE_REFERENCETYPE"]._serialized_end = 7480
    _globals["_WRITESETPAYLOAD"]._serialized_start = 7493
    _globals["_WRITESETPAYLOAD"]._serialized_end = 7561
    _globals["_ENTRYFUNCTIONID"]._serialized_start = 7563
    _globals["_ENTRYFUNCTIONID"]._serialized_end = 7646
    _globals["_MOVEMODULEID"]._serialized_start = 7648
    _globals["_MOVEMODULEID"]._serialized_end = 7693
    _globals["_MOVESTRUCTTAG"]._serialized_start = 7695
    _globals["_MOVESTRUCTTAG"]._serialized_end = 7818
    _globals["_SIGNATURE"]._serialized_start = 7821
    _globals["_SIGNATURE"]._serialized_end = 8369
    _globals["_SIGNATURE_TYPE"]._serialized_start = 8218
    _globals["_SIGNATURE_TYPE"]._serialized_end = 8356
    _globals["_ED25519SIGNATURE"]._serialized_start = 8371
    _globals["_ED25519SIGNATURE"]._serialized_end = 8428
    _globals["_MULTIED25519SIGNATURE"]._serialized_start = 8430
    _globals["_MULTIED25519SIGNATURE"]._serialized_end = 8541
    _globals["_MULTIAGENTSIGNATURE"]._serialized_start = 8544
    _globals["_MULTIAGENTSIGNATURE"]._serialized_end = 8724
    _globals["_FEEPAYERSIGNATURE"]._serialized_start = 8727
    _globals["_FEEPAYERSIGNATURE"]._serialized_end = 8998
    _globals["_SECP256K1ECDSASIGNATURE"]._serialized_start = 9000
    _globals["_SECP256K1ECDSASIGNATURE"]._serialized_end = 9064
    _globals["_ACCOUNTSIGNATURE"]._serialized_start = 9067
    _globals["_ACCOUNTSIGNATURE"]._serialized_end = 9458
    _globals["_ACCOUNTSIGNATURE_TYPE"]._serialized_start = 9349
    _globals["_ACCOUNTSIGNATURE_TYPE"]._serialized_end = 9445
# @@protoc_insertion_point(module_scope)
